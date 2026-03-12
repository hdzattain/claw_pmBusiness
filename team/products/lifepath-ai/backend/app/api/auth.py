from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, Field
from app.core.db import create_audit_log, create_user, get_user_by_email
from app.core.security import (
    create_access_token, 
    hash_password, 
    verify_password, 
    is_legacy_hash,
    migrate_legacy_password
)

router = APIRouter()


class ErrorSchema(BaseModel):
    code: str
    message: str


class ErrorResponse(BaseModel):
    success: bool = False
    error: ErrorSchema


class RegisterRequest(BaseModel):
    email: EmailStr = Field(examples=["student@example.com"])
    password: str = Field(min_length=8, max_length=128, examples=["12345678"])


class AuthResponse(BaseModel):
    success: bool
    token: str
    user: dict


@router.post(
    "/register",
    response_model=AuthResponse,
    responses={400: {"model": ErrorResponse}, 409: {"model": ErrorResponse}},
    summary="注册账号",
    description="创建新用户并返回 JWT token。",
)
def register(payload: RegisterRequest):
    if len(payload.password) < 8:
        raise HTTPException(status_code=400, detail="Password too short")

    existing = get_user_by_email(payload.email)
    if existing:
        raise HTTPException(status_code=409, detail="Email already exists")

    user_id = create_user(payload.email, hash_password(payload.password))
    token = create_access_token(user_id=user_id, email=payload.email)
    create_audit_log(user_id, "register", None, hash_password(payload.email))

    return {"success": True, "token": token, "user": {"id": user_id, "email": payload.email}}


class LoginRequest(BaseModel):
    email: EmailStr = Field(examples=["student@example.com"])
    password: str = Field(examples=["12345678"])


@router.post(
    "/login",
    response_model=AuthResponse,
    responses={401: {"model": ErrorResponse}},
    summary="用户登录",
    description="使用邮箱和密码登录，返回 JWT token。支持自动密码哈希迁移。",
)
def login(payload: LoginRequest):
    user = get_user_by_email(payload.email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # 验证密码
    password_valid = verify_password(payload.password, user["password_hash"])
    
    # 如果是旧的 SHA256 哈希格式，进行迁移
    if not password_valid and is_legacy_hash(user["password_hash"]):
        try:
            # 迁移密码哈希
            new_hash = migrate_legacy_password(payload.email, payload.password, user["password_hash"])
            
            # 更新数据库中的密码哈希
            from app.core.db import update_user_password_hash
            update_user_password_hash(user["id"], new_hash)
            
            # 重新验证新密码
            password_valid = True
            user["password_hash"] = new_hash
            
            # 记录审计日志
            create_audit_log(int(user["id"]), "password_migrated", None, hash_password(f"migrate_{payload.email}"))
            
        except Exception as e:
            # 迁移失败，仍然返回无效凭证错误
            pass
    
    if not password_valid:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(user_id=int(user["id"]), email=str(user["email"]))
    create_audit_log(int(user["id"]), "login", None, hash_password(payload.email))
    return {"success": True, "token": token, "user": {"id": user["id"], "email": user["email"]}}

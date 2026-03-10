from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, Field
from app.core.db import create_audit_log, create_user, get_user_by_email
from app.core.security import create_access_token, hash_password, verify_password

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
    description="使用邮箱和密码登录，返回 JWT token。",
)
def login(payload: LoginRequest):
    user = get_user_by_email(payload.email)
    if not user or not verify_password(payload.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(user_id=int(user["id"]), email=str(user["email"]))
    create_audit_log(int(user["id"]), "login", None, hash_password(payload.email))
    return {"success": True, "token": token, "user": {"id": user["id"], "email": user["email"]}}

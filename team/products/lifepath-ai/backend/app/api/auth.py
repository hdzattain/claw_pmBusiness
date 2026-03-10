from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, Field
from app.core.db import create_audit_log, create_user, get_user_by_email
from app.core.security import create_access_token, hash_password, verify_password

router = APIRouter()


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class AuthResponse(BaseModel):
    success: bool
    token: str
    user: dict


@router.post("/register")
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
    email: EmailStr
    password: str


@router.post("/login")
def login(payload: LoginRequest):
    user = get_user_by_email(payload.email)
    if not user or not verify_password(payload.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(user_id=int(user["id"]), email=str(user["email"]))
    create_audit_log(int(user["id"]), "login", None, hash_password(payload.email))
    return {"success": True, "token": token, "user": {"id": user["id"], "email": user["email"]}}

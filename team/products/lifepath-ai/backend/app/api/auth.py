from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr

router = APIRouter()


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


@router.post("/register")
def register(payload: RegisterRequest):
    # TODO: hash password, persist user
    if len(payload.password) < 8:
        raise HTTPException(status_code=400, detail="Password too short")
    return {"success": True, "message": "registered (stub)"}


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


@router.post("/login")
def login(payload: LoginRequest):
    # TODO: verify credentials + issue JWT
    return {"success": True, "token": "jwt-placeholder"}

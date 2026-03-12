import bcrypt
from datetime import datetime, timedelta, timezone
import jwt
from jwt import InvalidTokenError
from app.core.config import settings


def hash_password(password: str) -> str:
    """使用 bcrypt 对密码进行哈希处理"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def verify_password(password: str, password_hash: str) -> bool:
    """验证密码与哈希值是否匹配"""
    try:
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
    except Exception:
        return False


def is_legacy_hash(password_hash: str) -> bool:
    """判断是否为旧的 SHA256 哈希格式"""
    # SHA256 哈希长度为 64 位十六进制字符
    return len(password_hash) == 64 and all(c in '0123456789abcdef' for c in password_hash.lower())


def migrate_legacy_password(email: str, password: str, legacy_hash: str) -> str:
    """迁移旧的 SHA256 哈希到 bcrypt"""
    # 验证旧密码正确性
    import hashlib
    if hashlib.sha256(password.encode("utf-8")).hexdigest() != legacy_hash:
        raise ValueError("Password verification failed during migration")
    
    # 生成新的 bcrypt 哈希
    return hash_password(password)


def create_access_token(user_id: int, email: str) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(user_id),
        "email": email,
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(minutes=settings.jwt_exp_minutes)).timestamp()),
    }
    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)


def decode_access_token(token: str) -> dict:
    try:
        return jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
    except InvalidTokenError as exc:
        raise ValueError("Invalid token") from exc

import os
import logging

logger = logging.getLogger(__name__)


class Settings:
    def __init__(self):
        self.jwt_secret: str = os.getenv("LIFEPATH_JWT_SECRET", "change-me-in-prod")
        self.jwt_algorithm: str = "HS256"
        self.jwt_exp_minutes: int = int(os.getenv("LIFEPATH_JWT_EXP_MINUTES", "10080"))  # 7 days
        
        # 生产环境安全检查
        if not os.getenv("LIFEPATH_JWT_SECRET") and os.getenv("ENVIRONMENT", "development") != "development":
            logger.warning("⚠️  WARNING: Using default JWT secret in non-development environment!")
            logger.warning("⚠️  Please set LIFEPATH_JWT_SECRET environment variable for production!")


settings = Settings()

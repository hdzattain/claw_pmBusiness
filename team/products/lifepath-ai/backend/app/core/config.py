import os


class Settings:
    jwt_secret: str = os.getenv("LIFEPATH_JWT_SECRET", "change-me-in-prod")
    jwt_algorithm: str = "HS256"
    jwt_exp_minutes: int = int(os.getenv("LIFEPATH_JWT_EXP_MINUTES", "10080"))  # 7 days


settings = Settings()

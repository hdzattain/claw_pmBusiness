import os
from pathlib import Path


def _read_secret_file(path: Path) -> str:
    try:
        if path.exists():
            return path.read_text(encoding="utf-8").strip()
    except Exception:
        return ""
    return ""


class Settings:
    jwt_secret: str = os.getenv("LIFEPATH_JWT_SECRET", "change-me-in-prod")
    jwt_algorithm: str = "HS256"
    jwt_exp_minutes: int = int(os.getenv("LIFEPATH_JWT_EXP_MINUTES", "10080"))  # 7 days

    # model provider: heuristic | ollama | openai_compat
    model_provider: str = os.getenv("LIFEPATH_MODEL_PROVIDER", "heuristic")

    ollama_base_url: str = os.getenv("LIFEPATH_OLLAMA_BASE_URL", "http://127.0.0.1:11434")
    ollama_model: str = os.getenv("LIFEPATH_OLLAMA_MODEL", "qwen2.5:7b")

    openai_base_url: str = os.getenv("LIFEPATH_OPENAI_BASE_URL", "https://api.deepseek.com/v1")
    openai_model: str = os.getenv("LIFEPATH_OPENAI_MODEL", "deepseek-chat")
    openai_api_key: str = os.getenv(
        "LIFEPATH_OPENAI_API_KEY",
        _read_secret_file(Path.home() / ".openclaw" / "secret" / "selfdeployDeepSeekV3Key"),
    )


settings = Settings()

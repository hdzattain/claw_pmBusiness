from fastapi import APIRouter
from pydantic import BaseModel
from app.core.privacy import PrivacyInterceptor

router = APIRouter()
privacy = PrivacyInterceptor()


class AdviceInput(BaseModel):
    text: str
    mood: str | None = None
    goal: str | None = None


@router.post("/daily")
def daily_advice(payload: AdviceInput):
    intercepted = privacy.intercept_sensitive(payload.text)
    # TODO: call Mem0 + LLM
    return {
        "success": True,
        "today_action": "Spend 25 minutes updating your project portfolio.",
        "privacy": intercepted,
    }

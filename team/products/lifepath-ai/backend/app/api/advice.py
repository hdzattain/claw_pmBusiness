from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.api.dependencies import get_current_user
from app.core.db import create_audit_log, create_journal_entry, list_journal_entries
from app.core.privacy import PrivacyInterceptor

router = APIRouter()
privacy = PrivacyInterceptor()


class AdviceInput(BaseModel):
    text: str
    mood: str | None = None
    goal: str | None = None


@router.post("/daily")
def daily_advice(payload: AdviceInput, user: dict = Depends(get_current_user)):
    intercepted = privacy.intercept_sensitive(payload.text)

    create_journal_entry(
        user_id=int(user["id"]),
        text_masked=intercepted["masked_data"],
        raw_hash=privacy.hash_text(payload.text),
        mood=payload.mood,
        goal=payload.goal,
    )

    create_audit_log(
        user_id=int(user["id"]),
        action="advice_daily",
        privacy_proof=intercepted["proof"],
        payload_hash=privacy.hash_text(payload.text),
    )

    return {
        "success": True,
        "today_action": "今天先做一件最小可执行动作：用25分钟写出你的转型作品集第一页。",
        "privacy": intercepted,
    }


@router.get("/journal")
def get_journal(user: dict = Depends(get_current_user)):
    items = list_journal_entries(user_id=int(user["id"]), limit=30)
    return {"success": True, "items": items}

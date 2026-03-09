from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.api.dependencies import get_current_user
from app.core.db import create_audit_log, create_journal_entry, list_journal_entries
from app.core.privacy import PrivacyInterceptor
from app.core.recommendation import RecommendationInput, generate_evening_review, generate_morning_action

router = APIRouter()
privacy = PrivacyInterceptor()


class AdviceInput(BaseModel):
    text: str
    mood: str | None = None
    goal: str | None = None


class EveningInput(BaseModel):
    wins: str
    blockers: str
    next_action: str


@router.post("/daily")
def daily_advice(payload: AdviceInput, user: dict = Depends(get_current_user)):
    # Kept for backward compatibility; alias to /morning
    return morning_advice(payload, user)


@router.post("/morning")
def morning_advice(payload: AdviceInput, user: dict = Depends(get_current_user)):
    intercepted = privacy.intercept_sensitive(payload.text)
    history = list_journal_entries(user_id=int(user["id"]), limit=30)

    action = generate_morning_action(
        RecommendationInput(
            text=intercepted["masked_data"],
            mood=payload.mood,
            goal=payload.goal,
            history_count=len(history),
        )
    )

    create_journal_entry(
        user_id=int(user["id"]),
        text_masked=intercepted["masked_data"],
        raw_hash=privacy.hash_text(payload.text),
        mood=payload.mood,
        goal=payload.goal,
    )

    create_audit_log(
        user_id=int(user["id"]),
        action="advice_morning",
        privacy_proof=intercepted["proof"],
        payload_hash=privacy.hash_text(payload.text),
    )

    return {
        "success": True,
        "today_action": action,
        "privacy": intercepted,
        "history_count": len(history),
    }


@router.post("/evening")
def evening_review(payload: EveningInput, user: dict = Depends(get_current_user)):
    merged = f"wins:{payload.wins} blockers:{payload.blockers} next:{payload.next_action}"
    intercepted = privacy.intercept_sensitive(merged)
    review = generate_evening_review(payload.wins, payload.blockers, payload.next_action)

    create_journal_entry(
        user_id=int(user["id"]),
        text_masked=intercepted["masked_data"],
        raw_hash=privacy.hash_text(merged),
        mood="evening-review",
        goal=payload.next_action,
    )

    create_audit_log(
        user_id=int(user["id"]),
        action="advice_evening",
        privacy_proof=intercepted["proof"],
        payload_hash=privacy.hash_text(merged),
    )

    return {"success": True, "review": review, "privacy": intercepted}


@router.get("/journal")
def get_journal(user: dict = Depends(get_current_user)):
    items = list_journal_entries(user_id=int(user["id"]), limit=30)
    return {"success": True, "items": items}

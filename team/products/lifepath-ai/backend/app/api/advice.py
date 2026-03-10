from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from app.api.dependencies import get_current_user
from app.core.db import create_audit_log, create_journal_entry, list_journal_entries, count_journal_entries
from app.core.privacy import PrivacyInterceptor
from app.core.recommendation import RecommendationInput, generate_evening_review, generate_morning_action

router = APIRouter()
privacy = PrivacyInterceptor()


class AdviceInput(BaseModel):
    text: str = Field(min_length=1, max_length=2000, examples=["我今天不知道先做哪一件事"])
    mood: str | None = Field(default=None, max_length=60, examples=["有点焦虑"])
    goal: str | None = Field(default=None, max_length=200, examples=["今天完成简历首页"])


class EveningInput(BaseModel):
    wins: str = Field(min_length=1, max_length=800, examples=["完成了作品集首页"])
    blockers: str = Field(min_length=1, max_length=800, examples=["案例结构还不清楚"])
    next_action: str = Field(min_length=1, max_length=200, examples=["明早先补齐一个案例"])


@router.post(
    "/daily",
    summary="兼容旧接口：获取晨间建议",
    description="历史兼容接口，内部等价于 /morning。",
)
def daily_advice(payload: AdviceInput, user: dict = Depends(get_current_user)):
    # Kept for backward compatibility; alias to /morning
    return morning_advice(payload, user)


@router.post(
    "/morning",
    summary="晨间建议",
    description="输入今天的问题、心情、目标，返回今日最优行动建议。",
)
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


@router.post(
    "/evening",
    summary="晚间复盘",
    description="输入今日完成/阻塞/明日动作，返回复盘建议并写入记录。",
)
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


@router.get(
    "/journal",
    summary="获取复盘记录（分页）",
    description="支持 limit/offset 分页，返回 total 与 has_more。",
)
def get_journal(user: dict = Depends(get_current_user), limit: int = 30, offset: int = 0):
    safe_limit = max(1, min(limit, 100))
    safe_offset = max(0, offset)
    items = list_journal_entries(user_id=int(user["id"]), limit=safe_limit, offset=safe_offset)
    total = count_journal_entries(user_id=int(user["id"]))
    return {
        "success": True,
        "items": items,
        "pagination": {
            "limit": safe_limit,
            "offset": safe_offset,
            "total": total,
            "has_more": safe_offset + len(items) < total,
        },
    }

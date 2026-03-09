from dataclasses import dataclass


@dataclass
class RecommendationInput:
    text: str
    mood: str | None
    goal: str | None
    history_count: int


def generate_morning_action(data: RecommendationInput) -> str:
    mood = (data.mood or "").strip().lower()
    goal = (data.goal or "").strip()

    base = "先做一个25分钟、可完成、可验证的小动作。"

    if "焦虑" in mood or "anx" in mood:
        action = "先写下3个可控事项，然后只执行第1项25分钟。"
    elif "低" in mood or "sad" in mood:
        action = "先做最轻量任务：整理一页简历/作品集，再决定下一步。"
    else:
        action = "先输出一个可见成果：一页作品说明或一条对外展示内容。"

    if goal:
        action += f" 今日目标对齐：围绕“{goal[:40]}”完成最小交付。"

    if data.history_count == 0:
        action += " 你是第1次记录，今晚记得做复盘以建立节奏。"
    else:
        action += f" 你已累计记录 {data.history_count} 条，保持连续性优先。"

    return f"{base} {action}"


def generate_evening_review(wins: str, blockers: str, next_action: str) -> str:
    wins = wins.strip() or "今天有推进"
    blockers = blockers.strip() or "暂无明显阻塞"
    next_action = next_action.strip() or "明早继续25分钟推进"

    return (
        "晚间复盘：\n"
        f"- 今日完成：{wins}\n"
        f"- 主要阻塞：{blockers}\n"
        f"- 明日第一动作：{next_action}\n"
        "建议：明早先做“明日第一动作”，完成后再扩展任务。"
    )

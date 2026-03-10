from dataclasses import dataclass

from app.core.llm_adapter import generate_text


@dataclass
class RecommendationInput:
    text: str
    mood: str | None
    goal: str | None
    history_count: int


def generate_morning_action(data: RecommendationInput) -> str:
    mood = (data.mood or "").strip().lower()
    goal = (data.goal or "").strip()

    llm_prompt = (
        "请根据以下信息，输出一句中文行动建议，风格务实、可执行，且最好可在25分钟内开始。\n"
        f"问题: {data.text}\n"
        f"心情: {data.mood or '未填写'}\n"
        f"目标: {goal or '未填写'}\n"
        f"历史记录数: {data.history_count}\n"
        "要求：输出1-2句话，不要空话。"
    )
    llm_result = generate_text(prompt=llm_prompt, system_prompt="你是一个行动教练，强调可执行的小步骤。")
    if llm_result:
        return llm_result

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

    llm_prompt = (
        "请根据以下信息，输出一段简短晚间复盘（中文，4-6行，含建议）。\n"
        f"今日完成: {wins}\n"
        f"主要阻塞: {blockers}\n"
        f"明日第一动作: {next_action}\n"
        "请保留结构：今日完成/主要阻塞/明日第一动作/建议。"
    )
    llm_result = generate_text(prompt=llm_prompt, system_prompt="你是一个复盘教练，语气积极但不空泛。")
    if llm_result:
        return llm_result

    return (
        "晚间复盘：\n"
        f"- 今日完成：{wins}\n"
        f"- 主要阻塞：{blockers}\n"
        f"- 明日第一动作：{next_action}\n"
        "建议：明早先做“明日第一动作”，完成后再扩展任务。"
    )

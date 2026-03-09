from pydantic import BaseModel


class JournalEntry(BaseModel):
    content: str
    mood: str | None = None
    created_at: str | None = None


class ActionPlan(BaseModel):
    title: str
    why: str
    deadline: str | None = None

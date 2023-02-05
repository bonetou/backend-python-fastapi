from pydantic import BaseModel
from datetime import datetime


class Task(BaseModel):
    id: str
    title: str
    description: str | None = None
    completed: bool = False
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    tags: list[str] = []

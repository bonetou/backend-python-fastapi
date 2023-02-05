from pydantic import BaseModel
from pydantic import validator


class CreateTaskDTO(BaseModel):
    title: str
    description: str | None = None
    tags: list[str] = []

    @validator('title')
    def title_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError('title must not be blank')
        return v
    
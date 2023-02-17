from pydantic import BaseModel
from pydantic import validator


class CreateTaskDto(BaseModel):
    title: str
    description: str | None = None
    tags: list[str] = []

    @validator('title')
    def title_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError('title must not be blank')
        return v


class CreateUserDto(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError('username must not be blank')
        return v

    @validator('username')
    def username_should_only_contain_alphanumeric_characters(cls, v):
        if not v.isalnum():
            raise ValueError('username should only contain alphanumeric characters')
        return v

    @validator('password')
    def password_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError('password must not be blank')
        return v

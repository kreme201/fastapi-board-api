from datetime import datetime

from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    updated_at: datetime


class UserCreateDto(BaseModel):
    name: str
    email: str
    password: str


class UserUpdateDto(BaseModel):
    name: str | None
    password: str | None

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

from types.user_role import UserRole


class UserCreate(BaseModel):
    login: str


class UserUpdate(BaseModel):
    login: str | None
    telegram_id: int | None
    phone: str | None
    role: UserRole | None
    language: str | None


class UserRead(BaseModel):
    id: UUID
    login: str
    telegram_id: int | None
    phone: str | None
    role: UserRole
    language: str | None
    created_at: datetime

    class Config:
        from_attributes = True

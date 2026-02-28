from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Enum
from datetime import datetime, timezone


from db.models.base import Base
from db.models.mixins import UUIDMixin
from types.user_role import UserRole


class User(UUIDMixin, Base):
    """Пользователь системы."""

    __tablename__ = "user"

    telegram_id: Mapped[int | None]

    phone: Mapped[str | None]

    login: Mapped[str | None]

    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.RESEARCHER)

    language: Mapped[str] = mapped_column(String(10))

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )

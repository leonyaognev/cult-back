import uuid
from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import Base
from db.models.mixins import UUIDMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from db.models import User, Community, Event


class Comment(UUIDMixin, Base):
    __tablename__ = "comments"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"))
    community_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("communities.id"))
    event_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("events.id"), default=None
    )

    content: Mapped[str] = mapped_column(Text)
    rating: Mapped[int]

    user: Mapped["User"] = relationship("User")
    community: Mapped["Community"] = relationship(
        "Community", back_populates="comments"
    )
    event: Mapped["Event"] = relationship("Event", back_populates="comments")

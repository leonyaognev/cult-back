import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB

from db.models.base import Base
from db.models.mixins import UUIDMixin
from db.models.comment import Comment
from db.models.community_metrics import CommunityMetrics

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from db.models import CommunityTranslation
    from db.models import Culture
    from db.models import Event
    from db.models import User
    from db.models import Comment
    from db.models import CommunityMetrics


class Community(Base, UUIDMixin):
    __tablename__ = "communities"

    owner_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    culture_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("cultures.id"))
    metrics_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("community_metrics.id"))

    additional_info: Mapped[dict] = mapped_column(JSONB)

    community_translation: Mapped[list["CommunityTranslation"]] = relationship(
        "CommunityTranslation"
    )
    owner: Mapped["User"] = relationship("User")
    culture: Mapped["Culture"] = relationship("Culture")
    events: Mapped[list["Event"]] = relationship("Event", back_populates="community")
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="community")
    metrics: Mapped["CommunityMetrics"] = relationship("CommunityMetrics", uselist=False)

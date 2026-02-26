import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime
from db.models.mixins import UUIDMixin

from db.models.base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from db.models import Culture
    from db.models import Community
    from db.models import EventMetrics
    from db.models import EventTranslation


class Event(Base, UUIDMixin):
    __tablename__ = "events"

    community_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("communities.id"))
    culture_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("cultures.id"))

    start_datetime: Mapped[datetime]
    end_datetime: Mapped[datetime | None]
    registration_url: Mapped[str]
    media: Mapped[dict] = mapped_column(JSONB)

    event_translation: Mapped[list["EventTranslation"]] = relationship(
        "EventTranslation"
    )
    community: Mapped["Community"] = relationship("Community")
    culture: Mapped["Culture"] = relationship("Culture")
    metrics: Mapped[list["EventMetrics"]] = relationship("EventMetrics", uselist=False)

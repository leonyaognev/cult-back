import uuid

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from db.models.base import Base
from db.models.mixins import IntIdMixin

from types.locale import Locale


class EventTranslation(Base, IntIdMixin):
    __tablename__ = "cultures"

    event_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("event.id"))

    locale: Mapped[Locale]

    title: Mapped[str]
    short_description: Mapped[str]
    description: Mapped[str]

import uuid

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from db.models.base import Base
from db.models.mixins import IntIdMixin

from types.locale import Locale


class CommunityTranslation(Base, IntIdMixin):
    __tablename__ = "cultures"

    community_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("cultures.id"))

    locale: Mapped[Locale]

    title: Mapped[str]
    short_offer: Mapped[str]
    description: Mapped[str]
    external_url: Mapped[str]

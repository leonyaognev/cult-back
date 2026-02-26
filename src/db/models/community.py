import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB

from db.models.base import Base
from db.models.mixins import UUIDMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from db.models import CommunityTranslation
    from db.models import Culture
    from db.models import Event
    from db.models import User


class Community(Base, UUIDMixin):
    __tablename__ = "communities"

    owner_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    culture_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("cultures.id"))

    additional_info: Mapped[dict] = mapped_column(JSONB)

    community_translation: Mapped[list["CommunityTranslation"]] = relationship(
        "CommunityTranslation"
    )
    owner: Mapped["User"] = relationship("User")
    culture: Mapped["Culture"] = relationship("Culture")
    events: Mapped[list["Event"]] = relationship("Event", back_populates="community")

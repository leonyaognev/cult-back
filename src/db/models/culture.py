from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import Base
from db.models.mixins import IntIdMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from db.models.culture_translation import CultureTranslation


class Culture(Base, IntIdMixin):
    __tablename__ = "cultures"

    key: Mapped[str] = mapped_column(String, unique=True)

    culture_translation: Mapped[list["CultureTranslation"]] = relationship(
        "CultureTranslation"
    )

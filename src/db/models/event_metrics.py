import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.models.base import Base
from db.models.mixins.uuid_mixin import UUIDMixin


class EventMetrics(Base, UUIDMixin):
    __tablename__ = "event_metrics"

    views: Mapped[int] = mapped_column(default=0)
    clicks: Mapped[int] = mapped_column(default=0)
    registrations: Mapped[int] = mapped_column(default=0)

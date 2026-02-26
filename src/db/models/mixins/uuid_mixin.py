import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, declared_attr, mapped_column


class UUIDMixin:
    """Миксин, с первичным UUID ключом `id`."""

    @declared_attr
    def id(cls) -> Mapped[uuid.UUID]:
        """Идентефикатор."""
        return mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

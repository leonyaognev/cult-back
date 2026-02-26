from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, declared_attr, mapped_column


class IntIdMixin:
    """Миксин с первичным целочисленным ключом `id`."""

    @declared_attr
    def id(cls) -> Mapped[int]:
        """Идентификатор."""
        return mapped_column(Integer, primary_key=True, autoincrement=True)

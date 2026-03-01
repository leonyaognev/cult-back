from typing import Generic, List, Type, TypeVar
from sqlalchemy import select, delete, update

from db.utils import get_session

T = TypeVar("T")


class Repo(Generic[T]):
    """Репозиторий с заготовленным функционалом для работы с ORM моделями."""

    def __init__(self, model: Type[T]):
        self.model = model

    async def add(self, **kwargs) -> T:
        instance = self.model(**kwargs)
        async for session in get_session():
            async with session.begin():
                session.add(instance)
            return instance
        raise RuntimeError("Failed to get database session")

    async def get_all(self) -> List[T]:
        async for session in get_session():
            result = await session.execute(select(self.model))
            return result.scalars().unique().all()
        return []

    async def get_by_field(self, field: str, value) -> List[T]:
        async for session in get_session():
            if not hasattr(self.model, field):
                raise ValueError(
                    f"Field {field} not found in model {self.model.__name__}"
                )
            model_field = getattr(self.model, field)

            result = await session.execute(
                select(self.model).where(model_field == value)
            )
            return result.scalars().unique().all()
        return []

    async def update_by_field(self, field_name: str, value, **kwargs) -> int:
        async for session in get_session():
            if not hasattr(self.model, field_name):
                raise ValueError(
                    f"Field {field_name} not found in model {self.model.__name__}"
                )
            model_field = getattr(self.model, field_name)

            async with session.begin():
                result = await session.execute(
                    update(self.model)
                    .where(model_field == value)
                    .values(**kwargs)
                    .execution_options(synchronize_session="fetch")
                )
                return result.rowcount or 0
        return 0

    async def delete_by_field(self, field_name: str, value) -> int:
        async for session in get_session():
            model_field = getattr(self.model, field_name)
            if not model_field:
                raise ValueError(
                    f"Field {field_name} not found in model {self.model.__name__}"
                )

            async with session.begin():
                result = await session.execute(
                    delete(self.model).where(model_field == value)
                )
                return result.rowcount or 0
        return 0

from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from bot.config import settings
from bot.db.models import Base

engine = create_async_engine(settings.SQLALCHEMY_CONNECTION_STRING)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def close_db():
    """Закрывает соединение с базой данных."""
    await engine.dispose()

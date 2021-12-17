from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.session import async_session, sync_session


async def get_async_db() -> AsyncSession:
    """
    Dependency function that yields db sessions
    """
    async with async_session() as session:
        yield session
        await session.commit()


def get_db() -> Session:
    """
    Dependency function that yields db sessions
    """
    with sync_session() as session:
        yield session
        session.commit()

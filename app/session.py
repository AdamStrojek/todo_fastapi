from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings


async_engine = create_async_engine(
    settings.async_database_url,
    echo=settings.DB_ECHO_LOG,
)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DB_ECHO_LOG,
)
sync_session = sessionmaker(engine, expire_on_commit=False)

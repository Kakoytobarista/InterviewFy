from asyncio import current_task
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session
)

from .db_config import settings_db

import logging

from ...models.base_model import Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )
        logger.info("Database engine created")

    def get_scope_session(self):
        return async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )

    @asynccontextmanager
    async def get_db_session(self):
        from sqlalchemy import exc

        session: AsyncSession = self.session_factory()
        try:
            yield session
        except exc.SQLAlchemyError as error:
            logger.error(f"Error while getting db session, {error}")
            await session.rollback()
            raise
        finally:
            await session.close()


db_helper = DatabaseHelper(settings_db.database_url, settings_db.DB_ECHO_LOG)

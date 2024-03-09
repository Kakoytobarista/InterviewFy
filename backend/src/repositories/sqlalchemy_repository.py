import logging
from typing import Type, TypeVar, Optional, Generic, Callable, Any, Sequence, Dict

from pydantic import BaseModel
from sqlalchemy import delete, select, update, Row, RowMapping
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import join

from ..models.base_model import Base

from .base_repository import AbstractRepository


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SqlAlchemyRepository(AbstractRepository, Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType], db_session: Callable[[], AsyncSession]):
        self._session_factory = db_session
        self.model = model

    async def create(self, data: CreateSchemaType) -> ModelType:
        async with self._session_factory() as session:
            logger.info(f"Use create method with session {session}")
            instance = self.model(**data.dict())
            session.add(instance)
            await session.commit()
            logger.info("Commit was made")
            await session.refresh(instance)
            return instance

    async def update(self, data: UpdateSchemaType, **filters) -> ModelType:
        async with self._session_factory() as session:
            stmt = update(self.model).values(**data.dict()).filter_by(**filters).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def delete(self, **filters) -> None:
        async with self._session_factory() as session:
            await session.execute(delete(self.model).filter_by(**filters))
            await session.commit()

    async def get_single(self, **filters) -> Optional[ModelType] | None:
        async with self._session_factory() as session:
            row = await session.execute(select(self.model).filter_by(**filters))
            return row.scalar_one_or_none()

    async def get_multi(
            self,
            filters: Dict[str, Any] | None = None,
            order: str = "id",
            limit: int = 100,
            offset: int = 0
    ) -> Sequence[Row[Any] | RowMapping | Any]:
        async with self._session_factory() as session:
            stmt = select(self.model).order_by(order)
            if filters:
                stmt = stmt.where(**filters)
            stmt = stmt.limit(limit).offset(offset)

            rows = await session.execute(stmt)
            return rows.all()

    async def get_multi_with_join(
            self,
            join_model: Type[Any],
            on_condition: Any,
            filters: Dict[str, Any] | None = None,
            order: str = "id",
            limit: int = 100,
            offset: int = 0
    ) -> Sequence[Row[Any] | RowMapping | Any]:
        async with self._session_factory() as session:
            joined_stmt = join(self.model, join_model, on_condition)
            stmt = select(joined_stmt).order_by(order).distinct()
            if filters:
                stmt = stmt.where(**filters)
            stmt = stmt.limit(limit).offset(offset)

            rows = await session.execute(stmt)
            return rows.all()

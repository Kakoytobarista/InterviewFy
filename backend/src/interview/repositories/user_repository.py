from sqlalchemy import select
from sqlalchemy.orm import load_only


from ..schemas.user_schema import CategoryCreate, CategoryUpdate
from ...config.database.db_helper import db_helper
from ...models.user_model import UserModel
from ...repositories.sqlalchemy_repository import SqlAlchemyRepository, ModelType


class UserRepository(SqlAlchemyRepository[ModelType, CategoryCreate, CategoryUpdate]):

    async def filter(
        self,
        fields: list[str] | None = None,
        order: list[str] | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[ModelType] | None:
        async with self._session_factory() as session:
            stmt = select(self.model)
            if fields:
                model_fields = [getattr(self.model, field) for field in fields]
                stmt = stmt.options(load_only(*model_fields))
            if order:
                stmt = stmt.order_by(*order)
            if limit is not None:
                stmt = stmt.limit(limit)
            if offset is not None:
                stmt = stmt.offset(offset)

            row = await session.execute(stmt)
            return row.scalars().all()

    async def all(self) -> list[ModelType] | None:
        return await self.filter()

    async def create_user(self, ) -> bool:
        new_user = await self.create(data=data)
        async with self._session_factory as session:
            result = await session.execute(new_user)
            return result.scalar() is not None


category_repository = UserRepository(model=UserModel, db_session=db_helper.get_db_session)

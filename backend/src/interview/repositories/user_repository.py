import logging
from typing import Any, Sequence, Optional

from sqlalchemy import Row, RowMapping


from ..schemas.user_schema import UserCreate, UserUpdate
from ...config.database.db_helper import db_helper
from ...models.user_model import UserModel
from ...repositories.sqlalchemy_repository import SqlAlchemyRepository, ModelType

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class UserRepository(SqlAlchemyRepository[ModelType, UserCreate, UserUpdate]):

    async def all(self) -> Sequence[Row[Any] | RowMapping | Any]:
        return await self.get_multi()

    async def create_user(self, data: UserCreate) -> UserModel:
        existing_user = await self.get_existing_user(data)
        if existing_user:
            return existing_user
        else:
            new_user = await self.create(data=data)
            return new_user

    async def get_existing_user(self, data: UserCreate) -> Optional[UserModel]:
        existing_user = await self.get_single(full_name=data.full_name)
        return existing_user


user_repository = UserRepository(model=UserModel, db_session=db_helper.get_db_session)

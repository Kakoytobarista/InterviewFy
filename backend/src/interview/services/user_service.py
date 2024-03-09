from ..repositories.user_repository import user_repository
from ..schemas.user_schema import UserCreate
from ...repositories.sqlalchemy_repository import ModelType
from ...services.base_service import BaseService


class UserService(BaseService):

    async def filter(
            self,
            fields: list[str] | None = None,
            order: list[str] | None = None,
            limit: int | None = None,
            offset: int | None = None
    ) -> list[ModelType] | None:
        return await self.repository.filter(
            fields=fields,
            order=order,
            limit=limit,
            offset=offset
        )

    async def create_user(self, data: UserCreate) -> UserCreate:
        return await self.repository.create_user(data=data)


user_service = UserService(repository=user_repository)

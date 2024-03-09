from backend.src.interview.repositories.interview_repository import interview_repository
from backend.src.interview.schemas.interview_schema import InterviewCreate, InterviewListResponse
from backend.src.repositories.sqlalchemy_repository import ModelType
from backend.src.services.base_service import BaseService


class InterviewService(BaseService):

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

    async def get_all_interviews(self) -> InterviewListResponse | None:
        return await self.repository.get_all_interviews()

    async def create_interview(self, data) -> InterviewCreate:
        return await self.repository.create_interview(data=data)


interview_service = InterviewService(repository=interview_repository)

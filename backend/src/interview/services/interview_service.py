from src.interview.repositories.interview_repository import interview_repository
from src.interview.schemas.interview_schema import InterviewCreate, InterviewListResponse
from src.repositories.sqlalchemy_repository import ModelType
from src.services.base_service import BaseService


class InterviewService(BaseService):

    async def get_all_interviews(self) -> InterviewListResponse | None:
        return await self.repository.get_all_interviews()

    async def create_interview(self, data) -> InterviewCreate:
        return await self.repository.create_interview(data=data)


interview_service = InterviewService(repository=interview_repository)

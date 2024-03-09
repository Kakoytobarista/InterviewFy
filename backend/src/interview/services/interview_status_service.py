from backend.src.interview.repositories.interview_status_repository import interview_status_repository
from backend.src.interview.schemas.interview_status import InterviewStatusUpdate
from backend.src.repositories.sqlalchemy_repository import ModelType
from backend.src.schemas.interview_status_schema import InterviewStatusResponse
from backend.src.services.base_service import BaseService


class InterviewStatusService(BaseService):

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

    async def create_interview_status(self, data) -> InterviewStatusResponse:
        return await self.repository.create_interview_status(data=data)

    async def update_interview_status(self, data, interview_status_id) -> InterviewStatusUpdate:
        return await self.repository.update_interview_status(data=data, interview_status_id=interview_status_id)


interview_status_service = InterviewStatusService(repository=interview_status_repository)

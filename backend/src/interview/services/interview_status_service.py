from src.interview.repositories.interview_status_repository import interview_status_repository
from src.interview.schemas.interview_status import InterviewStatusUpdate, InterviewStatusResponse
from src.services.base_service import BaseService


class InterviewStatusService(BaseService):

    async def create_interview_status(self, data) -> InterviewStatusResponse:
        return await self.repository.create_interview_status(data=data)

    async def update_interview_status(self, data, interview_status_id) -> InterviewStatusUpdate:
        return await self.repository.update_interview_status(data=data, interview_status_id=interview_status_id)


interview_status_service = InterviewStatusService(repository=interview_status_repository)

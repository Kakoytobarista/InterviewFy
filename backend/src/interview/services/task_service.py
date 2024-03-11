from src.interview.repositories.task_repository import task_repository
from src.interview.schemas.task_schema import TaskCreate, TaskListResponse, TaskResponse
from src.repositories.sqlalchemy_repository import ModelType
from src.services.base_service import BaseService


class TaskService(BaseService):

    async def get_all_tasks(self) -> TaskListResponse:
        return await self.repository.get_all_tasks()

    async def get_all_tasks_by_interview_id(self, interview_id) -> TaskListResponse:
        return await self.repository.get_all_tasks_by_interview_id(interview_id=interview_id)

    async def create_task(self, data) -> TaskCreate:
        return await self.repository.create_task(data)


task_service = TaskService(repository=task_repository)

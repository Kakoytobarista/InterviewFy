from backend.src.interview.repositories.task_repository import task_repository
from backend.src.interview.schemas.task_schema import TaskCreate, TaskListResponse, TaskResponse
from backend.src.repositories.sqlalchemy_repository import ModelType
from backend.src.services.base_service import BaseService


class TaskService(BaseService):

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

    async def get_all_tasks(self) -> TaskListResponse:
        return await self.repository.get_all_tasks()

    async def get_all_tasks_by_interview_id(self, interview_id) -> TaskListResponse:
        return await self.repository.get_all_tasks_by_interview_id(interview_id=interview_id)

    async def create_task(self, data) -> TaskCreate:
        return await self.repository.create_task(data)


task_service = TaskService(repository=task_repository)

from sqlalchemy import select

from ..schemas.task_schema import TaskCreate, TaskUpdate, TaskListResponse, TaskResponse
from ...config.database.db_helper import db_helper
from ...models.interview_model import TaskModel, interview_task_association
from ...repositories.sqlalchemy_repository import SqlAlchemyRepository, ModelType


class TaskRepository(SqlAlchemyRepository[ModelType, TaskCreate, TaskUpdate]):

    async def get_all_tasks(self) -> TaskListResponse:
        tasks = await self.get_multi()
        task_responses = []
        for task in tasks:
            task_response = TaskResponse(name=task.name, content=task.content)
            task_responses.append(task_response)
        return TaskListResponse(tasks=task_responses)

    async def get_all_tasks_by_interview_id(self, interview_id: int) -> TaskListResponse:
        async with self._session_factory() as session:
            stmt = (
                select(TaskModel)
                .join(interview_task_association, TaskModel.id == interview_task_association.c.task_id)
                .where(interview_task_association.c.interview_id == interview_id)
            )
            result = await session.execute(stmt)
            tasks = [TaskResponse(name=row.name, content=row.content) for row in result.scalars().all()]
            return TaskListResponse(tasks=tasks)

    async def create_task(self, data: TaskCreate) -> TaskCreate:
        new_task = await self.create(data=data)
        return new_task


task_repository = TaskRepository(model=TaskModel, db_session=db_helper.get_db_session)

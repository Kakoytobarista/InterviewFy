import logging

from backend.src.config.database.db_helper import db_helper
from backend.src.interview.schemas.interview_schema import InterviewCreate, InterviewUpdate, InterviewListResponse, \
    SingleInterviewResponse
from backend.src.models.interview_model import InterviewModel, TaskModel
from backend.src.repositories.sqlalchemy_repository import SqlAlchemyRepository, ModelType


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class InterviewRepository(SqlAlchemyRepository[ModelType, InterviewCreate, InterviewUpdate]):

    async def get_all_interviews(self) -> InterviewListResponse | None:
        interview = await self.get_multi()
        interview_responses = []
        for interview in interview:
            interview_response = SingleInterviewResponse(name=interview.name, id=interview.id)
            interview_responses.append(interview_response)
        return InterviewListResponse(interviews=interview_responses)

    async def create_interview(self, data: InterviewCreate) -> InterviewModel:
        async with self._session_factory() as session:
            interview = InterviewModel(
                name=data.name)
            session.add(interview)

            for task_data in data.tasks:
                task = await session.get(TaskModel, task_data.id)
                if task:
                    interview.tasks.append(task)
                else:
                    logger.warning(f"Task with id {task_data.id} not found")
                    raise ValueError(f"Task with id {task_data.id} not found")

            await session.commit()
            await session.refresh(interview)
            return interview


interview_repository = InterviewRepository(model=InterviewModel, db_session=db_helper.get_db_session)

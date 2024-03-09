from typing import Any, Sequence

from sqlalchemy import Row, RowMapping

from backend.src.config.database.db_helper import db_helper
from backend.src.interview.schemas.interview_status import InterviewStatusCreate, InterviewStatusUpdate
from backend.src.models.interview_status_model import InterviewStatusModel
from backend.src.repositories.sqlalchemy_repository import SqlAlchemyRepository, ModelType
from backend.src.schemas.interview_status_schema import InterviewStatusResponse


class InterviewStatusRepository(SqlAlchemyRepository[ModelType, InterviewStatusCreate, InterviewStatusUpdate]):

    async def all(self) -> Sequence[Row[Any] | RowMapping | Any]:
        return await self.get_multi()

    async def create_interview_status(self, data: InterviewStatusCreate) -> InterviewStatusResponse:
        new_interview_status = await self.create(data=data)
        return new_interview_status

    async def update_interview_status(self, data: InterviewStatusUpdate, interview_status_id: int) -> bool:
        new_interview_status = await self.update(data=data, id=interview_status_id)
        return new_interview_status


interview_status_repository = InterviewStatusRepository(model=InterviewStatusModel, db_session=db_helper.get_db_session)

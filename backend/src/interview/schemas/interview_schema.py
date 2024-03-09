from typing import List

from pydantic import BaseModel

from backend.src.interview.schemas.task_schema import TaskInterviewCreate
from backend.src.schemas.base_schema import BaseSchema


class InterviewBase(BaseSchema):
    name: str
    tasks: List[TaskInterviewCreate]


class InterviewCreate(InterviewBase):
    pass


class InterviewCreateResponse(InterviewCreate):
    pass


class InterviewUpdate(InterviewBase):
    pass


class SingleInterviewResponse(BaseModel):
    id: int
    name: str

class InterviewListResponse(BaseModel):
    interviews: List[SingleInterviewResponse]

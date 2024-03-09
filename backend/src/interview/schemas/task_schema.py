from typing import List

from pydantic import BaseModel


class TaskBase(BaseModel):
    name: str
    content: str


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class TaskResponse(TaskBase):
    pass


class TaskListResponse(BaseModel):
    tasks: List[TaskResponse]


class TaskInterviewCreate(BaseModel):
    id: int

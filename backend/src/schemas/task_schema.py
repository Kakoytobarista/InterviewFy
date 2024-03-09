from .base_schema import BaseSchema


class Task(BaseSchema):
    id: int
    name: str
    content: str


class TaskCreateInterview(BaseSchema):
    id: int

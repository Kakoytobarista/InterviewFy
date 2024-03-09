from .base_schema import BaseSchema


class InterviewStatus(BaseSchema):
    id: int
    interview_id: int
    user_id: int
    is_passed: bool | None
    score: float | None

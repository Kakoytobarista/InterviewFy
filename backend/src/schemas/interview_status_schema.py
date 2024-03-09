from .base_schema import BaseSchema


class InterviewStatusResponse(BaseSchema):
    id: int
    interview_id: int
    user_id: int
    is_passed: bool
    score: float

from src.schemas.base_schema import BaseSchema


class InterviewProcessResponse(BaseSchema):
    id: int
    interview_id: int
    user_id: int


class InterviewProcessCreate(BaseSchema):
    interview_id: int
    full_name: str


class InterviewProcessCreateResponse(BaseSchema):
    id: int
    interview_id: int
    user_id: int
    score: float = 0
    is_passed: bool = False

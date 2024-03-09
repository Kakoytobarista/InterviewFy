from backend.src.schemas.base_schema import BaseSchema


class InterviewProcessResponse(BaseSchema):
    id: int
    interview_id: int
    user_id: int
    full_name: str


class InterviewProcessCreate(BaseSchema):
    interview_id: int
    full_name: str


class InterviewProcessCreateResponse(BaseSchema):
    interview_id: int
    user_id: int

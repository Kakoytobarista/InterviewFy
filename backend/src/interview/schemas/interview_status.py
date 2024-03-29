from src.schemas.base_schema import BaseSchema


class InterviewStatusBase(BaseSchema):
    interview_id: int
    user_id: int
    is_passed: bool = False
    score: float | None = 0


class InterviewStatusResponse(InterviewStatusBase):
    pass


class InterviewStatusCreate(InterviewStatusBase):
    pass


class InterviewStatusUpdate(BaseSchema):
    is_passed: bool = False
    score: float

class InterviewStatusUpdateResponse(InterviewStatusUpdate):
    pass

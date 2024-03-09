from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from ..schemas.interview_process_schema import InterviewProcessResponse, InterviewProcessCreate, \
    InterviewProcessCreateResponse
from ..schemas.interview_status import InterviewStatusCreate
from ..schemas.user_schema import UserCreate
from ..services.interview_status_service import interview_status_service
from ..services.user_service import user_service

router = APIRouter(prefix='/interview_process', tags=["interview_process"])


@router.post("/start_interview", response_model=InterviewProcessCreateResponse)
async def create_interview_process(data: InterviewProcessCreate) -> InterviewProcessCreateResponse:
    try:
        user_data = await user_service.create_user(UserCreate(full_name=data.full_name))
        user_id = user_data.id
        interview_status = await interview_status_service.create_interview_status(
            InterviewProcessCreateResponse(interview_id=data.interview_id,
                                           user_id=user_id))
        return interview_status
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))

from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from ..schemas.interview_status import InterviewStatusCreate, InterviewStatusUpdate
from ..services.interview_status_service import interview_status_service
from ...schemas.interview_status_schema import InterviewStatusResponse

router = APIRouter(prefix='/intreview_status', tags=["intreview_status"])


@router.post("/create_interview_status", response_model=InterviewStatusResponse)
async def create_interview_status(data: InterviewStatusCreate) -> InterviewStatusResponse:
    try:
        return await interview_status_service.create_interview_status(data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.patch("/update_interview_status/{interview_status_id}", response_model=InterviewStatusUpdate)
async def update_interview_status(data: InterviewStatusUpdate, interview_status_id: int) -> InterviewStatusUpdate:
    try:
        return await interview_status_service.update_interview_status(data, interview_status_id)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))

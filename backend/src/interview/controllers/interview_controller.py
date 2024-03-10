from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from backend.src.interview.schemas.interview_schema import (InterviewCreate,
                                                            InterviewCreateResponse, InterviewListResponse)
from backend.src.interview.services.interview_service import interview_service

router = APIRouter(prefix='/interview', tags=["interview"])


@router.get("/get_all", response_model=InterviewListResponse)
async def get_all():
    try:
        return await interview_service.get_all_interviews()
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.post("/create_interview", response_model=InterviewCreateResponse)
async def create_interview(data: InterviewCreate) -> InterviewCreateResponse:
    try:
        return await interview_service.create_interview(data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))

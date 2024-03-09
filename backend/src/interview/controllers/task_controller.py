from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from ..schemas.task_schema import TaskCreate, TaskListResponse
from ..services.task_service import task_service

router = APIRouter(prefix='/task', tags=["task"])


@router.post("/create_task", response_model=TaskCreate)
async def create_task(data: TaskCreate) -> TaskCreate:
    try:
        return await task_service.create_task(data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.post("/get_all", response_model=TaskListResponse)
async def get_all():
    try:
        return await task_service.get_all_tasks()
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.get("/get_all/{interview_id}", response_model=TaskListResponse)
async def get_all_by_interview_id(interview_id: int):
    try:
        return await task_service.get_all_tasks_by_interview_id(interview_id=interview_id)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))

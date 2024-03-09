from typing import Annotated

from fastapi import HTTPException, Query, APIRouter
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from ..schemas.user_schema import UserCreate
from ..services.user_service import user_service

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/create_user", response_model=UserCreate)
async def create_user(data: UserCreate) -> UserCreate:
    try:
        return await user_service.create_user(data)
    except Exception as e:
        print(dir(e))
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e.orig))

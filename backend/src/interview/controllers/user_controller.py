from fastapi import HTTPException, APIRouter
from starlette.status import HTTP_400_BAD_REQUEST

from ..schemas.user_schema import UserCreate, UserCreateResponse
from ..services.user_service import user_service

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/create_user", response_model=UserCreateResponse)
async def create_user(data: UserCreate) -> UserCreateResponse:
    try:
        return await user_service.create_user(data)
    except Exception as e:
        print(dir(e))
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e.orig))

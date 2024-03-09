from backend.src.schemas.base_schema import BaseSchema


class UserBase(BaseSchema):
    full_name: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserResponse(UserBase):
    pass


class UserListResponse(BaseSchema):
    type: str | None = None

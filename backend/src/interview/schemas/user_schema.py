from src.schemas.base_schema import BaseSchema


class UserBase(BaseSchema):
    full_name: str


class UserCreate(UserBase):
    pass

class UserCreateResponse(UserCreate):
    pass

class UserUpdate(UserBase):
    pass

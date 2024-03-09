from typing import NewType

from pydantic import BaseModel

PyModel = NewType("PyModel", BaseModel)


class BaseSchema(BaseModel):
    pass

    class Config:
        from_attributes = True

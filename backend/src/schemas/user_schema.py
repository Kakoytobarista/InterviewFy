from pydantic import BaseModel

class User(BaseModel):
    full_name: str
    type: str

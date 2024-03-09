from typing import List

from .base_schema import BaseSchema


class Interview(BaseSchema):
    tasks_id: List[int]

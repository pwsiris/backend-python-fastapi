from datetime import date
from typing import Optional

from pydantic import BaseModel


class NewGame(BaseModel):
    name: str
    link: str
    status: str
    order_by: Optional[int] = None
    genre: int


class UpdateGame(BaseModel):
    status: Optional[str]
    genre: Optional[int]
    comment: Optional[str]
    completed_date: Optional[str]
    score: Optional[float]
    records: Optional[dict]

    def dict_info(self):
        info = {}
        for field, value in self:
            if value:
                info[field] = value
                if field == "completed_date":
                    info[field] = date.fromisoformat(value)
        return info

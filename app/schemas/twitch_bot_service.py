from pydantic import BaseModel

# from typing import Optional


class NewItem(BaseModel):
    string: str


class UpdateItem(BaseModel):
    id: int
    string: str


class DeleteItem(BaseModel):
    id: int


class Cheats(BaseModel):
    enable: bool

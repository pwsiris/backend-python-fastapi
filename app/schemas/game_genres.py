from pydantic import BaseModel


class GameGenre(BaseModel):
    name: str

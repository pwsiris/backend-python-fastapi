from crud import games as games_crud
from db.session import get_session
from fastapi import APIRouter, Depends
from schemas import games as games_schemas

from . import HTTPanswer

router = APIRouter()


@router.post("/game")
async def add_game(new_game: games_schemas.NewGame, session=Depends(get_session)):
    game_id = await games_crud.add_game(session, new_game)
    return HTTPanswer(201, game_id)


@router.get("/game/{id}")
async def get_game(id: int, session=Depends(get_session)):
    return await games_crud.get_game(session, id)


@router.put("/game/{id}")
async def update_game(
    id: int, game_data: games_schemas.UpdateGame, session=Depends(get_session)
):
    await games_crud.update_game(session, id, game_data)
    return HTTPanswer(200, "Updated")


@router.get("/games")
async def get_games(
    limit: int = 0, offset: int = 0, genre: str = "", session=Depends(get_session)
):
    return await games_crud.get_games(session, genre, limit, offset)

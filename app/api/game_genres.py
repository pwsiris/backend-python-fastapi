from crud import game_genres as game_genres_crud
from db.session import get_session
from fastapi import APIRouter, Depends
from schemas import game_genres as game_genres_schemas

from . import HTTPanswer

router = APIRouter()


@router.post("/game_genre")
async def add_game_genre(
    new_game_genre: game_genres_schemas.GameGenre, session=Depends(get_session)
):
    game_genre_id = await game_genres_crud.add_game_genre(session, new_game_genre.name)
    return HTTPanswer(201, game_genre_id)


@router.delete("/game_genre/{id}")
async def delete_game_genre(id: int, session=Depends(get_session)):
    await game_genres_crud.delete_game_genre(session, id)
    return HTTPanswer(200, "OK")


@router.put("/game_genre/{id}")
async def updste_game_genre(
    id: int, genre: game_genres_schemas.GameGenre, session=Depends(get_session)
):
    await game_genres_crud.update_game_genre(session, id, genre.new_name)
    return HTTPanswer(200, "OK")


@router.get("/game_genres")
async def get_game_genres(session=Depends(get_session)):
    return await game_genres_crud.get_game_genres(session)

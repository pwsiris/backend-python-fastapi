from db.models import Game, GameGenre
from sqlalchemy import delete, select, update
from utils.errors import HTTPabort


async def add_game_genre(session, name):
    async with session.begin():
        game_genre_id = await session.scalar(
            select(GameGenre.id).where(GameGenre.name == name)
        )
        if game_genre_id:
            HTTPabort(409, "Genre already exists!")

        genre = GameGenre(name=name)
        session.add(genre)
        await session.flush()
        await session.refresh(genre)
        return genre.id


async def delete_game_genre(session, id):
    async with session.begin():
        game_genre_id = await session.scalar(
            select(GameGenre.id).where(GameGenre.id == id)
        )
        if not game_genre_id:
            HTTPabort(404, "Genre not found!")
        await session.execute(delete(GameGenre).where(GameGenre.id == game_genre_id))
        await session.execute(
            update(Game).where(Game.genre == game_genre_id).values(genre=None)
        )


async def update_game_genre(session, id, new_name):
    async with session.begin():
        game_genre_id = await session.scalar(
            select(GameGenre.id).where(GameGenre.id == id)
        )
        if not game_genre_id:
            HTTPabort(404, "Genre not found!")

        await session.execute(
            update(GameGenre).where(GameGenre.id == game_genre_id).values(name=new_name)
        )


async def get_game_genres(session):
    async with session.begin():
        genres = (await session.scalars(select(GameGenre))).all()
        return {"count": len(genres), "data": genres}

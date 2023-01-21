from datetime import date

from db.models import Game, GameGenre, User
from sqlalchemy import join, select, update
from utils.errors import HTTPabort


async def add_game(session, new_game):
    async with session.begin():
        game_id = await session.scalar(
            select(Game.id).where(Game.name == new_game.name)
        )
        if game_id:
            HTTPabort(409, "Game already exists!")

        game = Game(
            name=new_game.name,
            link=new_game.link,
            status=new_game.status,
            order_by=new_game.order_by,
            genre=new_game.genre,
            added_date=date.today(),
        )
        session.add(game)
        await session.flush()
        await session.refresh(game)
        return game.id


async def get_game(session, game_id):
    async with session.begin():
        info = (
            await session.execute(
                select(
                    Game.id,
                    Game.name,
                    User.name.label("order_by"),
                    Game.link,
                    Game.status,
                    Game.comment,
                    Game.added_date,
                    Game.completed_date,
                    Game.score,
                    Game.records,
                    GameGenre.name.label("genre"),
                )
                .select_from(
                    join(Game, User, Game.order_by == User.id, isouter=True,).join(
                        GameGenre,
                        Game.genre == GameGenre.id,
                        isouter=True,
                    )
                )
                .where(Game.id == game_id)
            )
        ).first()

        if not info:
            HTTPabort(404, "Game not found!")
        return info


async def update_game(session, id, game_data):
    async with session.begin():
        game_id = await session.scalar(select(Game.id).where(Game.id == id))
        if not game_id:
            HTTPabort(404, "Game not found!")

        # update_data = {}
        # for field, value in game_data:
        #     if value:
        #         update_data[field] = value
        #         if field == "completed_date":
        #             update_data[field] = date.fromisoformat(value)

        await session.execute(
            update(Game).where(Game.id == id)
            # .values(update_data)
            .values(game_data.dict_info())
        )


async def get_games(session, genre, limit, offset):
    async with session.begin():
        query = select(
            Game.id,
            Game.name,
            User.name.label("order_by"),
            Game.link,
            Game.status,
            Game.comment,
            Game.added_date,
            Game.completed_date,
            Game.score,
            Game.records,
            GameGenre.name.label("genre"),
        ).select_from(
            join(Game, User, Game.order_by == User.id, isouter=True,).join(
                GameGenre,
                Game.genre == GameGenre.id,
                isouter=True,
            )
        )

        if genre:
            genre_id = await session.scalar(
                select(GameGenre.id).where(GameGenre.name == genre)
            )
            if not genre_id:
                HTTPabort(404, "Unknown genre!")

            query = query.where(Game.genre == genre)

        if offset >= 0 and limit > 0:
            query = query.offset(offset).limit(limit)

        games = (await session.execute(query)).all()
        return {"count": len(games), "data": games}

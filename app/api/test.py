from db.models import Test

# rom . import schemas
# from . import logic
# from .config import cfg
from db.session import get_session, get_session_2
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.sql import text

router = APIRouter()


@router.get("/test")
async def test(session=Depends(get_session)):
    async with session.begin():
        await session.execute(
            text(
                "CREATE TABLE IF NOT EXISTS TEST (id SERIAL PRIMARY KEY, text VARCHAR);"
            )
        )
        await session.execute(text("INSERT INTO TEST VALUES (2, 'qwer');"))
        await session.execute(text("INSERT INTO TEST VALUES (1, 'asdf');"))
        answer = await session.execute(text("SELECT version();"))
        answer = await session.execute(select(Test))
        print(answer)
    # await session.commit()
    return {"answer": answer}


@router.get("/test2")
async def test2(session=Depends(get_session_2)):
    async with session.begin():
        answer = await session.execute(select(Test))
        print(answer.scalars().all())

        answer2 = (await session.scalars(select(Test))).all()
        print(answer2)

    # await session.commit()
    return {"answer": "answer"}

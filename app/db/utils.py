from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from .session import _engine  # , get_session, get_session_2,


async def check_db():
    try:
        async with AsyncSession(_engine, expire_on_commit=False) as session:
            answer = await session.execute(text("SELECT version();"))
            print(
                f"INFO:\tSuccessfully connecting to database.\n\t{answer.first()}",
                flush=True,
            )
    except Exception as e:
        print(f"ERROR:\tFailed to connect to database:\n{str(e)}", flush=True)
        raise

    # try:
    #     async with get_session() as session:
    #         answer = await session.execute(text("SELECT version();"))
    #         print(f'INFO:\tSuccessfully connecting to database.\n\t{answer.first()}', flush=True)
    # except Exception as e:
    #     print(f'ERROR:\tFailed to connect to database:\n{str(e)}', flush=True)

    # s = get_session_2()
    # answer = await s.execute(text("SELECT version();"))
    # print(f"INFO:\tSuccessfully connecting to database.\n\t{answer.first()}", flush=True)

    # session = get_session_2()
    # await session.execute(text("SELECT version();"))
    # print(f'INFO:\tSuccessfully connecting to database.\n\t{answer.first()}', flush=True)
    # try:
    #     session = await get_session_2()
    #     await session.execute(text("SELECT version();"))
    #     print(f'INFO:\tSuccessfully connecting to database.\n\t{answer.first()}', flush=True)
    # except Exception as e:
    #     print(f'ERROR:\tFailed to connect to database:\n{str(e)}', flush=True)

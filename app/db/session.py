from sqlalchemy.ext.asyncio import (  # , async_sessionmaker
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

# from contextlib import asynccontextmanager
from utils.config import cfg

_engine = create_async_engine(cfg.DB_CONNECTION_STRING, future=True)
# _session = async_sessionmaker(_engine, expire_on_commit=False)
_session = sessionmaker(_engine, expire_on_commit=False, class_=AsyncSession)


# @asynccontextmanager
# async def get_session():
#     session = _session()
#     try:
#         yield session
#         session.commit()
#     except:
#         session.rollback()
#         raise
#     finally:
#         session.close()


async def get_session():
    async with AsyncSession(_engine, expire_on_commit=False) as session:
        yield session


async def get_session_2():
    async with _session() as session:
        yield session

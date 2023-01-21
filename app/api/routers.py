from fastapi import APIRouter

from .game_genres import router as game_genres_router
from .games import router as games_router
from .test import router as test_router
from .twitch_bot import router as twitch_bot_router
from .twitch_bot_service import router as twitch_bot_service_router

routers = APIRouter()


routers.include_router(games_router)
routers.include_router(game_genres_router)

routers.include_router(test_router, prefix="/test")
routers.include_router(twitch_bot_router, prefix="/twitch_bot")
routers.include_router(twitch_bot_service_router, prefix="/twitch_bot_service")

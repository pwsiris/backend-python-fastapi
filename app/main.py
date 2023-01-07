import uvicorn
from fastapi import FastAPI
from utils.config import YamlConfigManager, cfg
from utils.errors import exception_handlers

# import logging


ConfigManager = YamlConfigManager(interval=60)

FastAPP = FastAPI(exception_handlers=exception_handlers)


@FastAPP.on_event("startup")
async def startup():
    await ConfigManager.start(cfg)
    print("INFO:\tConfig was loaded")

    from db import check_db

    await check_db()

    from api import test, twitch_bot

    FastAPP.include_router(test.router, prefix="/tests")
    FastAPP.include_router(twitch_bot.router, prefix="/twitch_bot")


@FastAPP.on_event("shutdown")
async def shutdown():
    from db.session import _engine

    await _engine.dispose()


if __name__ == "__main__":
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"][
        "fmt"
    ] = "%(asctime)s - %(client_addr)s - '%(request_line)s' %(status_code)s"

    uvicorn.run(
        "main:FastAPP",
        #        uds="/tmp/pwsi_uvicorn.sock",
        host="0.0.0.0",
        port=8008,
        log_config=log_config,
        reload=True,
    )

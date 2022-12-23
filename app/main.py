from argparse import ArgumentParser

import uvicorn
from fastapi import FastAPI
from utils.config import YamlConfigManager, cfg

ConfigManager = YamlConfigManager(interval=60)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await ConfigManager.start(cfg)


@app.on_event("shutdown")
async def shutdown():
    pass


if __name__ == "__main__":
    parser = ArgumentParser(description="FastAPI backend")
    parser.add_argument(
        "-H", "--host", required=True, action="store", dest="host", help="Server host"
    )
    parser.add_argument(
        "-P", "--port", required=True, action="store", dest="port", help="Server port"
    )

    args = parser.parse_args()

    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"][
        "fmt"
    ] = '%(asctime)s - %(client_addr)s - "%(request_line)s" %(status_code)s'

    uvicorn.run(
        app, host=args.host, port=int(args.port), log_config=log_config, reload=False
    )

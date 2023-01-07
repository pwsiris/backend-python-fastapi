from fastapi.responses import JSONResponse
from utils.config import cfg


def HTTPanswer(status_code, description, action_cookie=None, token=None):
    response = JSONResponse(
        status_code=status_code,
        content={"content": description},
    )
    if action_cookie == "set":
        response.set_cookie(
            key=cfg.TOKEN_NAME,
            value=token,
            path="/",
            domain=cfg.DOMAIN,
            httponly=True,
            samesite=None,
        )
    elif action_cookie == "delete":
        response.delete_cookie(cfg.TOKEN_NAME, path="/", domain=cfg.DOMAIN)

    return response

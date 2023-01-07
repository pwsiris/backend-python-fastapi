from fastapi import HTTPException


def HTTPabort(status_code, description):
    raise HTTPException(status_code=status_code, detail=description)


exception_handlers = {}

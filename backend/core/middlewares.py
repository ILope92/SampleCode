from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi import status


async def http_exception_handler_func(request: Request, exception: HTTPException):
    # BAD REQUEST
    if exception.status_code == status.HTTP_400_BAD_REQUEST:
        return JSONResponse(
            content={"Error": exception.detail}, status_code=exception.status_code
        )


exception_handlers = {HTTPException: http_exception_handler_func}

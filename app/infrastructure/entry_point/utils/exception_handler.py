from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.domain.model.util.custom_exceptions import CustomException

async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.http_status,
        content={
            "apiCode": exc.code,
            "data": None,
            "message": exc.message,
            "status": exc.http_status == 200
        }
    )

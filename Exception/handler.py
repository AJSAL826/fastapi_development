from fastapi.exceptions import RequestValidationError
from fastapi import Request, status
from fastapi.responses import JSONResponse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class CustomException(Exception):
    def __init__(self, details, status_code, function):
        self.details = details
        self.status_code = status_code
        self.function = function

        # super().__init__(self.details, self, status_code)


class CustomHandler:
    @staticmethod
    async def CustomhandlerRequedtError(req: Request, exc: RequestValidationError):
        status_code = status.HTTP_400_BAD_REQUEST
        data = {
            "input": exc.errors()[0].get("input"),
            "message": exc.errors()[0].get("msg"),
            "status_code": 400,
        }
        return JSONResponse(content={**data}, status_code=status_code)

    @staticmethod
    async def CustomHandlerException(req: Request, exc: CustomException):
        # print("handler_exception", exc.status_code)
        status_code = (
            status.HTTP_500_INTERNAL_SERVER_ERROR
            if exc.status_code != 404
            else status.HTTP_404_NOT_FOUND
        )
        # print(exc.function, exc.details, status_code)
        data = {
            "function": str(exc.function),
            "details": str(exc.details),
            "status_code": exc.status_code,
            "request_method": req.method,
        }
        return JSONResponse(content={**data}, status_code=status_code)


async def common_exception(e=None, error=0, function=None):
    if error:
        error = 0
        raise CustomException(
            details="Data not found",
            status_code=404,
            function=function,
        )
    else:
        raise CustomException(details=f"{repr(e)}", status_code=500, function=function)

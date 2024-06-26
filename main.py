from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from udemy.user import router
from Exception.handler import CustomHandler, CustomException

app = FastAPI()

app.add_exception_handler(
    RequestValidationError, CustomHandler.CustomhandlerRequedtError
)
app.add_exception_handler(CustomException, CustomHandler.CustomHandlerException)


app.include_router(router, prefix="/post_and_comments", tags=["post and comments"])

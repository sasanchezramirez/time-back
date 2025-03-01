from fastapi import FastAPI
from app.application.container import Container
from app.application.handler import Handlers



def create_app():
    container = Container()
    fast_api = FastAPI()
    fast_api.container = container 
    for handler in Handlers.iterator():
        fast_api.include_router(handler.router)
    return fast_api
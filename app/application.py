from fastapi import FastAPI

from database import SqlAlchemySessionMiddleware
from .web import router


def create_app() -> FastAPI:
    fastapi = FastAPI()

    fastapi.add_middleware(SqlAlchemySessionMiddleware)

    fastapi.include_router(router)

    return fastapi


app = create_app()

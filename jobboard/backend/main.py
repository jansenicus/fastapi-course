from fastapi import FastAPI
from jobboard.backend.core.config import settings
from jobboard.backend.db.session import engine
from jobboard.backend.db.base import Base
from jobboard.backend.apis.base import api_router

def init_tables():

    Base.metadata.create_all(bind=engine)


def include_router(app):
    pass

def start_application():

    app = FastAPI(title=settings.PROJECT_TITLE,
                  version=settings.PROJECT_VERSION)

    init_tables()

    app.include_router(api_router)


    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"detail": "Hello World!"}

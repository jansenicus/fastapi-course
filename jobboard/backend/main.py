from fastapi import FastAPI
from jobboard.backend.core.config import settings
from jobboard.backend.db.session import engine
from jobboard.backend.db.base import Base
from jobboard.backend.apis.v1.route_users import router

def init_tables():

    Base.metadata.create_all(bind=engine)


def start_application():

    app = FastAPI(title=settings.PROJECT_TITLE,
                  version=settings.PROJECT_VERSION)

    init_tables()

    app.include_router(router)


    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"detail": "Hello World!"}

from fastapi import FastAPI
from jobboard.backend.core.config import settings
from jobboard.backend.db.session import engine
from jobboard.backend.db.base_class import Base


def create_tables():

    Base.metadata.create_all(bind=engine)


def start_application():

    app = FastAPI(title=settings.PROJECT_TITLE,
                  version=settings.PROJECT_VERSION)

    create_tables()

    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"detail": "Hello World!"}

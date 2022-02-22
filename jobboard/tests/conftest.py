import pytest
from typing import (Any, Generator)
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.apis.base import api_router
from backend.db.session import (SQL_ALCHEMY_DATABASE_URL, get_db)
from backend.db.base import Base

def start_application():
    app = FastAPI()
    app.include_router(api_router)
    return app


SQL_ALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQL_ALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})

SessionTesting = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    """
    create a fresh database on each test case.
    """
    Base.metadata.create_all(engine)  # create tables
    _app = start_application()
    yield _app
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session  # using session in test
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(
    app: FastAPI, db_session: SessionTesting
) -> Generator[TestClient, Any, None]:
    """
    create a new FastAPI TestClient that uses the `db_session` fixture to override the `get_db` dependency 
    that is injected into routes.
    """
    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db()
    with TestClient(app) as client:
        yield client

from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.core.config import settings

SQL_ALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

# SQL_ALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
# engine = create_engine( SQL_ALCHEMY_DATABASE_URL,
#                         connect_args={'check_same_thread':
#                                      False})

SessionLocal = sessionmaker(autocommit=False,
                             autoflush=False,
                             bind=engine)

def get_db() -> Generator:
    """
    returns a generator
    for local session 
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
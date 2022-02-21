from sqlalchemy import (Column,
                        Integer,
                        String,
                        Boolean)
from sqlalchemy.orm import relationship
from jobboard.backend.db.base_class import Base


class User(Base):
    """
    represents a database object: the `User` table
    """
    id = Column(Integer,
                primary_key=True,
                index=True)
    username = Column(String,
                      unique=True,
                      nullable=False)
    email = Column(String, nullable=False,
                   unique=True,
                   index=True)
    hashed_password = Column(String,
                             nullable=False)
    is_active = Column(Boolean(),
                       default=True)
    is_superuser = Column(Boolean(),
                          default=False)
    jobs = relationship("Job",
                        back_populates="owner")

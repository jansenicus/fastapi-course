from pydoc import describe
from sqlalchemy import (Column,
                        Integer,
                        String,
                        Boolean,
                        Date,
                        ForeignKey)
from sqlalchemy.orm import relationship
from jobboard.backend.db.base_class import Base


class Job(Base):
    """
    represents a database object: the `Job` table
    """
    id = Column(Integer,
                primary_key=True,
                index=True)
    title = Column(String,
                   nullable=False)
    company = Column(String,
                     nullable=False)
    company_url = Column(String)
    location = Column(String,
                      nullable=False)
    description = Column(String)
    date_posted = Column(Date)
    is_active = Column(Boolean(),
                       default=True)
    owner_id = Column(Integer,
                      ForeignKey('user.id'))
    owner = relationship("User",
                         back_populates="jobs")

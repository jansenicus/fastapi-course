from fastapi import (APIRouter,
                     Depends)
from sqlalchemy.orm import Session

from jobboard.backend.schemas.users import UserCreate
from jobboard.backend.db.session import get_db
from jobboard.backend.db.repository.users import create_new_user

router = APIRouter()


@router.post("/")
def create_user(user: UserCreate, db: Session=Depends(get_db)):
    user = create_new_user(user, db)
    return user

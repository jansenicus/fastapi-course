from sqlalchemy.orm import Session

from jobboard.backend.schemas.users import UserCreate
from jobboard.backend.db.models.users import User
from jobboard.backend.core.hashing import Hasher


def create_new_user(user: UserCreate, db: Session):
    user = User(username=user.username,
                email=user.email,
                hashed_password=Hasher.get_password_hash(user.password),
                is_active=True,
                is_superuser=False
                )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

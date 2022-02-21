from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """
    validation schema to validate User Object upon User Creation attempt
    EmailStr requires pydantic[email] package
    """
    username: str
    email: EmailStr
    password: str


class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    
    class Config():
        orm_mode = True

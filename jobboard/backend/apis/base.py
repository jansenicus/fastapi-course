from fastapi import APIRouter
from jobboard.backend.apis.v1 import route_users

api_router = APIRouter()

api_router.include_router(route_users.router,
                          prefix="/user",
                          tags=["user"])

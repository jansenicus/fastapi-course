from fastapi import APIRouter
from backend.apis.v1 import (route_users, route_jobs)

api_router = APIRouter()

api_router.include_router(route_users.router,
                          prefix="/user",
                          tags=["user"])

api_router.include_router(route_jobs.router,
                          prefix="/job",
                          tags=["job"])
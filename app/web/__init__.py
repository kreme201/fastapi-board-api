from fastapi import APIRouter

from .user.endpoints import router as user_router

router = APIRouter()

router.include_router(user_router, prefix="/api/users", tags=["User"])

__all__ = [
    router,
]

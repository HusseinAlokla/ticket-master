from fastapi import APIRouter

router = APIRouter()

@router.get("/users/me")
async def read_current_user():
    return {"message": "User info would go here"}


### app/routes/__init__.py
from fastapi import APIRouter
from .event_routes import router as event_router
from .user_controller import router as user_router

router = APIRouter()
router.include_router(event_router)
router.include_router(user_router)
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.deps import get_db
from app.services.event_service import get_all_events, store_event
from app.services.ticketmaster import fetch_events_from_ticketmaster
from app.schemas import EventSchema
from typing import List
from app.auth.deps import get_current_user
from app.services.event_service import save_event_for_user
from app.services.event_service import get_saved_events


router = APIRouter()

@router.get("/events", response_model=List[EventSchema])
async def list_events(db: AsyncSession = Depends(get_db)):
    return await get_all_events(db)

@router.post("/events/fetch")
async def fetch_and_store_events(db: AsyncSession = Depends(get_db)):
    events = await fetch_events_from_ticketmaster()
    for event in events:
        await store_event(event, db)
    return {"message": f"Stored {len(events)} events."}

@router.get("/my/events", response_model=List[EventSchema])
async def get_my_events(user=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    user_id = user["sub"]
    return await get_saved_events(user_id, db)

@router.post("/events/{event_id}/save")
async def save_event_to_user(event_id: str, user=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    user_id = user["sub"]
    return await save_event_for_user(user_id, event_id, db)
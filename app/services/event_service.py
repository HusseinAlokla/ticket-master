from app.models.event import Event
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from typing import List
from datetime import datetime
from app.models.user_event import UserEvent






async def get_all_events(db: AsyncSession) -> List[Event]:
    result = await db.execute(select(Event))
    return result.scalars().all()


async def store_event(event_data: dict, db: AsyncSession):
    event_id = event_data["id"]
    name = event_data["name"]
    date_str = event_data.get("dates", {}).get("start", {}).get("dateTime")
    date = None
    if date_str:
        try:
            date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))  # ✅ Convert Z to UTC offset
        except Exception as e:
            print("❌ Failed to parse date:", date_str, e)
    image_url = event_data["images"][0]["url"] if event_data.get("images") else None
    venue = event_data.get("_embedded", {}).get("venues", [{}])[0].get("name")

    event = Event(id=event_id, name=name, date=date, image_url=image_url, venue=venue)

    try:
        db.add(event)
        await db.commit()
    except IntegrityError:
        await db.rollback()  # Duplicate, already stored

async def get_saved_events(user_id: str, db: AsyncSession) -> List[Event]:
    result = await db.execute(
        select(Event)
        .join(UserEvent, UserEvent.event_id == Event.id)
        .where(UserEvent.user_id == user_id)
    )
    return result.scalars().all()

async def save_event_for_user(user_id: int, event_id: str, db: AsyncSession):
    user_event = UserEvent(user_id=user_id, event_id=event_id)
    try:
        db.add(user_event)
        await db.commit()
        return {"message": "Event saved"}
    except Exception as e:
        await db.rollback()
        return {"error": str(e)}

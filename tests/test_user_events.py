from app.services.event_service import save_event_for_user, get_saved_events
import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_save_event_for_user(db_session):
    user_id = "user123"
    event_id = "test123"
    
    await save_event_for_user(user_id, event_id, db_session)
    saved = await get_saved_events(user_id, db_session)
    
    assert any(e.id == event_id for e in saved)

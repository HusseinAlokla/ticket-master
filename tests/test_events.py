import pytest
from app.services.ticketmaster import fetch_events_from_ticketmaster
from app.services.event_service import store_event, get_all_events

@pytest.mark.asyncio
async def test_fetch_events_from_ticketmaster():
    events = await fetch_events_from_ticketmaster()
    assert isinstance(events, list)
    assert "name" in events[0]

@pytest.mark.asyncio
async def test_store_and_retrieve_event(db_session):
    event_data = {
        "id": "test123",
        "name": "Test Event",
        "dates": {"start": {"dateTime": "2025-12-25T18:00:00Z"}},
        "images": [{"url": "http://example.com/image.jpg"}],
        "_embedded": {"venues": [{"name": "Test Venue"}]}
    }

    await store_event(event_data, db_session)
    events = await get_all_events(db_session)
    assert any(e.id == "test123" for e in events)

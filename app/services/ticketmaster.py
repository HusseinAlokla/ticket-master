import httpx
import os

TICKETMASTER_API_KEY = os.getenv("TICKETMASTER_API_KEY")
print("✅ Loaded API key:", TICKETMASTER_API_KEY)  # Add this

async def fetch_events_from_ticketmaster(keyword: str = "music", size: int = 10):
    url = "https://app.ticketmaster.com/discovery/v2/events.json"
    params = {
        "apikey": TICKETMASTER_API_KEY,
        "keyword": keyword,
        "size": size,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        print("🔍 Ticketmaster response status:", response.status_code)
        data = response.json()
        print("📦 Ticketmaster raw data:", data)  # Add this

        events = data.get("_embedded", {}).get("events", [])
        print(f"🎫 Found {len(events)} events")
        return events

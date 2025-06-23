from fastapi import FastAPI
from app.db.session import Base, engine
from app.models import User, Event, UserEvent
from sqlalchemy.ext.asyncio import AsyncEngine
import asyncio
from app.routes import router as main_router

app = FastAPI(title="Ticketmaster Backend API")


async def wait_for_db(engine: AsyncEngine, retries: int = 10, delay: int = 2):
    for i in range(retries):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(lambda x: None)  # Simple no-op to test DB connection
            print("✅ Database connection established")
            return
        except Exception as e:
            print(f"⏳ Waiting for DB... ({i+1}/{retries}) - {e}")
            await asyncio.sleep(delay)
    raise Exception("❌ Could not connect to the database after retries")


@app.on_event("startup")
async def on_startup():
    await wait_for_db(engine)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # Create tables on startup
    print("📦 Tables created")

app.include_router(main_router)


@app.get("/")
async def root():
    return {"message": "API is running"}

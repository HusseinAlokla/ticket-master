from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+aiomysql://user:password@db:3306/ticketdb")

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


Base = declarative_base()
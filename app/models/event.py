from sqlalchemy import Column, String, DateTime
from app.db.session import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(String(100), primary_key=True, index=True)  # Ticketmaster ID
    name = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=True)
    image_url = Column(String(500), nullable=True)
    venue = Column(String(255), nullable=True)

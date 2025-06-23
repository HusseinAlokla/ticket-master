from sqlalchemy import Column, ForeignKey, UniqueConstraint, String, Integer
from app.db.session import Base

class UserEvent(Base):
    __tablename__ = "user_events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(255), ForeignKey("users.auth0_id"), nullable=False)
    event_id = Column(String(100), ForeignKey("events.id"), nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'event_id', name='uix_user_event'),
    )

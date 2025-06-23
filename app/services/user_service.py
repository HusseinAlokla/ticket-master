from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User
from sqlalchemy.future import select

async def get_user_by_auth0(db: AsyncSession, auth0_id: str):
    result = await db.execute(select(User).where(User.auth0_id == auth0_id))
    return result.scalar_one_or_none()
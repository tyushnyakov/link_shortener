from app.models import Url
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


async def create_url(session: AsyncSession, url: str):
    db_url = Url(url=url)
    session.add(db_url)
    await session.commit()
    return db_url.id


async def get_url(session: AsyncSession, uuid: str):
    result = await session.execute(select(Url).where(Url.id == uuid))
    url = result.scalars().first()
    if url:
        return url.url
    return None

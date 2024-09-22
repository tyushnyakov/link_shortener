from fastapi import Depends, FastAPI, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.crud import create_url, get_url
from app.schemas import UrlCreate

app = FastAPI()


@app.post("/shorten", response_model=str)
async def shorten_url(url: UrlCreate, request: Request, session: AsyncSession = Depends(get_session)):
    result = await create_url(session, url.url)
    return str(request.base_url) + result


@app.get("/{uuid}", response_model=str)
async def redirect_to_url(uuid: str, session: AsyncSession = Depends(get_session)):
    url = await get_url(session, uuid)
    return RedirectResponse(url)

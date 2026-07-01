from fastapi import FastAPI

from contextlib import asynccontextmanager

from app.config import TITLE, DESCRIPTION, VERSION
from app.routes import router
from app.database import database

@asynccontextmanager
async def lifespan(app: FastAPI):
      database.connect()
      yield
      database.disconnect()

app = FastAPI(
      title=TITLE,
      description=DESCRIPTION,
      version=VERSION,
      lifespan=lifespan
)

app.include_router(router)
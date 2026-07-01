from fastapi import FastAPI

from app.config import TITLE, DESCRIPTION, VERSION
from app.routes import router

# Settings (your)

app = FastAPI(
      title=TITLE,
      description=DESCRIPTION,
      version=VERSION
)

app.include_router(router)
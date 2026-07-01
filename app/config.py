import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))

TITLE = os.getenv("TITLE", "FastAPI Template")
DESCRIPTION = os.getenv("DESCRIPTION", "")
VERSION = os.getenv("VERSION", "1.0.0")

DEBUG = os.getenv("DEBUG", "False").lower() == "true"
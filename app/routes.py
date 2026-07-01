from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def home():
      return {
            "message": "Hello, World!"
      }

@router.get("/status")
async def status():
      return {
            "status": "OK (200)"
      }
      
"""
Your functions...
"""
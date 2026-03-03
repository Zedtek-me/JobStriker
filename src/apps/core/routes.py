from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/health", tags=["Core"])
async def health_check():
    return {"status": "ok"}

@router.get("/home")
async def core_home():
    return {"message": "Welcome to Core In Job Striker!"}

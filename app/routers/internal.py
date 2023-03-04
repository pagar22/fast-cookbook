from fastapi import APIRouter

router = APIRouter(prefix="/internal", tags=["internal"])


@router.get("/ping")
def ping():
    return {"data": "ping!"}

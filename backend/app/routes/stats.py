from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_placeholder():
    return {"msg": "Stats route placeholder"}

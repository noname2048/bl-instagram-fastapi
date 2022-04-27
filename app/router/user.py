from fastapi import APIRouter
from fastapi import Depends

router = APIRouter(prefix="/user", tags=["user"])

# create_user
@router.post("")
async def create_user():
    pass

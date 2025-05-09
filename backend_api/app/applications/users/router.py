from fastapi import APIRouter, status
from sqlalchemy.ext.asyncio import AsyncSession
from applications.users.schemas import BaseFields, RegisterUserFields
from settings import settings

router_users = APIRouter()


@router_users.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(new_user: RegisterUserFields, session: AsyncSession) -> BaseFields:
    print(settings.POSTGRES_DB, 6666666666666666666666)
    return new_user

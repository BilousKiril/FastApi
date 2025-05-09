from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from applications.users.models import User
from applications.users.schemas import BaseFields, RegisterUserFields
from database.session_dependancies import get_async_session
from settings import settings

router_users = APIRouter()


async def create_user(email, name, password, session: AsyncSession):
    new_user = User(email=email, name=name, hashed_password=password)
    session.add(new_user)
    await session.commit()


@router_users.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(new_user: RegisterUserFields, session: AsyncSession = Depends(get_async_session)) -> BaseFields:
    print(session)

    return new_user

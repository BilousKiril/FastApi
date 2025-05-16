from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from applications.auth.password_handler import PasswordEndcrypt
from applications.users.models import User
from applications.users.schemas import BaseFields, RegisterUserFields
from database.session_dependancies import get_async_session




async def create_user_in_db(email, name, password, session: AsyncSession):

    hashed_password = await PasswordEndcrypt.get_password_hash(password)
    new_user = User(email=email, name=name, hashed_password=hashed_password)
    session.add(new_user)
    await session.commit()

async def get_user_by_email(email, session: AsyncSession) -> User | None:
    query = select(User).filter(User.email == email)
    result = await session.execute(query)
    return result.scalar_one_or_none()
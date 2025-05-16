from applications.users.crud import get_user_by_email
from settings import settings
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from applications.auth.password_handler import PasswordEndcrypt
from sqlalchemy.ext.asyncio import AsyncSession


from database.session_dependancies import get_async_session

class AuthHandler:
    def __init__(self):
        self.secret = settings.JWT_SECRET
        self.algorithm = settings.JWT_ALGORITHM
    async def get_login_token_pairs(self, data: OAuth2PasswordRequestForm, session: AsyncSession):
        user_email = data.username
        user_password = data.password
        user = await get_user_by_email(user_email, session)
        print(user, 888888)

        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User not found')

        is_valid_password = await PasswordEndcrypt.verify_password(user_password, user.hashed_password)
        if not is_valid_password:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Incorrect password')
auth_handler = AuthHandler()

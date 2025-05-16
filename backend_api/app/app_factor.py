from fastapi import FastAPI

from applications.users.router import router_users
from applications.auth.router import router_users, router_auth
from settings import settings


def get_application():

    app = FastAPI(root_path="/api", root_path_in_servers=True, debug=settings.DEBUG)
    app.include_router(router_users, prefix="/users", tags=["Users"])
    app.include_router(router_auth, prefix="/users", tags=["Auth"])
    return app

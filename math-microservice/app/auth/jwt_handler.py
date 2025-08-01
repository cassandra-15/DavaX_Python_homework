# Placeholder content for jwt_handler.py
# app/auth/jwt_handler.py
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = "supersecret"


@AuthJWT.load_config
def get_config():
    return Settings()

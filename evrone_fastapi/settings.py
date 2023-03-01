"""
    Settings
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """ Settings class """
    main_url: str

    # class Config:
    #     env_prefix = 'app_'
    #     fields = {"environment": {"env": "ENV_TYPE"}}


settings = Settings()

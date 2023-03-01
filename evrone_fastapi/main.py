"""
    Main
"""
from fastapi import FastAPI
from pydantic import BaseModel
from .settings import settings


app = FastAPI()


class Status(BaseModel):
    """ Status response """
    status: str = "OK"


@app.get(settings.main_url)
async def root():
    """ Root method """
    return Status()

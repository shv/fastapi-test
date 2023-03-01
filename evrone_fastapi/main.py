"""
    Main
"""
from fastapi import FastAPI
from pydantic import BaseModel
from .settings import settings
import logging


app = FastAPI()


class Status(BaseModel):
    """ Status response """
    status: str = "OK"

logging.error(f"1: {settings.main_url}")
print("1", settings.main_url)

@app.get(settings.main_url)
async def root():
    """ Root method """
    return Status()

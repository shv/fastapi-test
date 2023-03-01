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


class Form(BaseModel):
    """ Request form """
    firstname: str
    lastname: str
    age: int


class FormResult(BaseModel):
    """ Result response """
    message: str


@app.get(settings.main_url)
async def root():
    """ Root method """
    return Status()


@app.post("/create-message")
async def create_message(form: Form):
    """ Create message """
    message = f"{form.firstname} {form.lastname}: {form.age} years old."
    result = FormResult(message=message)
    return result

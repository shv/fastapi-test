# pull official base image
FROM python:3.11.2-alpine

EXPOSE 8000
# set work directory
WORKDIR /code

RUN pip install --upgrade pip
RUN apk add gcc musl-dev libffi-dev
RUN pip install poetry

COPY . /code

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --without test

CMD ["poetry", "run", "uvicorn", "evrone_fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:alpine

WORKDIR /usr/src/crud

RUN apk update

RUN apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirements.txt /usr/src/crud/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /usr/src/crud

CMD [ "fastapi", "run", "main.py" ]
FROM python:alpine3.19

WORKDIR /usr/src/crud

RUN apk update && apk add --no-cache \
    gcc \
    libc-dev \
    libffi-dev \
    musl-dev \
    python3-dev \
    postgresql-dev

COPY ./requirements.txt /usr/src/crud/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /usr/src/crud

CMD [ "fastapi", "run", "main.py" ]
FROM python:3.12-alpine3.20

WORKDIR /usr/src/crud

COPY ./requirements.txt /usr/src/crud/requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY ./src /usr/src/crud

CMD [ "fastapi", "run", "main.py" ]
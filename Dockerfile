FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY image_app /image_app
WORKDIR /image_app
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password image_app-user

USER image_app-user
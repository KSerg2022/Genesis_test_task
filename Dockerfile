FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y upgrade

WORKDIR /code

COPY . /code

RUN pip install -r /code/requirements.txt

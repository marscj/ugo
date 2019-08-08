FROM python:latest
LABEL maintainer ugodubai
ENV PYTHONUNBUFFERED 1
RUN mkdir /docker_api
WORKDIR /docker_api
COPY . /docker_api
RUN apt-get update && apt-get install vim
RUN pip install --upgrade pip && pip install -r requirements.txt
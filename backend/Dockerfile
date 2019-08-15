FROM python:latest
LABEL maintainer ugodubai
ENV PYTHONUNBUFFERED 1
RUN mkdir /website
WORKDIR /website
COPY . /website
# RUN apt-get update && apt-get install vim
RUN pip install --upgrade pip && pip install -r requirements.txt
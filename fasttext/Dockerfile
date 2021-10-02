# Get image
FROM python:3.7-slim

WORKDIR app

COPY ./fasttext/models /app/models
COPY ./fasttext/main.py /app/
COPY ./fasttext/languagedetection.py /app/
COPY ./fasttext/requirements.txt /app/

RUN apt-get update 
RUN apt-get install g++ gcc -y

# Install environment dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

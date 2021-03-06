# Pull base image
FROM python:3.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install requirements.txt

COPY . /code/

EXPOSE 8000
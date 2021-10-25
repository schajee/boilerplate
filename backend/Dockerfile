# pull official base image
FROM python:3.7-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y python3-pip python3-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN sed -i 's/\r$//g' ./entrypoint
RUN chmod +x ./entrypoint

ENTRYPOINT ["./entrypoint"]
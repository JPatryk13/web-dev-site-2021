# pull official base image
FROM python:3.8.6-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
# install Pillow dependencies
    && apk add --virtual build-deps \
    && apk add jpeg-dev zlib-dev libjpeg \
# install Pillow
    && pip install Pillow \
# remove build-deps
    && apk del build-deps \
# install libsass deps
    && apk add build-base

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements/ ./requirements/
RUN pip install -r requirements/dev.txt

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

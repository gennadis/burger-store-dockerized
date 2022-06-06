###########
# BUILDER #
###########

# pull official base image
FROM python:3.9-alpine as builder

# set work directory
WORKDIR /usr/src/app

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.9-alpine

# create directory for the app user
RUN mkdir -p /home/app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy project
COPY . $APP_HOME


# BUILD STAGE
FROM python:3.9-alpine as builder

WORKDIR /usr/src/app

# include postgres and pillow dependencies
RUN apk update && apk add --no-cache \
    gcc \
    # postgres dependencies
    python3-dev \
    postgresql-dev \
    libpq-dev \
    musl-dev \
    # pillow dependencies
    jpeg-dev \
    zlib-dev

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

# RELEASE STAGE
FROM python:3.9-alpine

WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/wheels /wheels

RUN apk update && apk add --no-cache libpq
RUN pip install --upgrade pip --no-cache /wheels/*


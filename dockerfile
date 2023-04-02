FROM python:3.8-buster
RUN pip install pipenv

# Begin our actual build
# FROM base as base1
# collectstatic needs the secret key to be set. We store that in this environment variable.
# Set this value in this project's .env file
# ARG DJANGO_SECRET_KEY

RUN mkdir -p /app

COPY . /app
COPY Pipfile  /app/
COPY Pipfile.lock /app/

WORKDIR /app

RUN pipenv install --system --deploy
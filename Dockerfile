# Pull base image and give it an alias 'python_base'
FROM docker.io/python:3.12.9-slim-bookworm AS python_base

# To Do: figure out how to put migrations and compilation into a separate stage
#  - https://docs.docker.com/build/building/multi-stage/
#  - to build stage to minimize setup time

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set work directory called `code`
RUN mkdir -p /code
WORKDIR /code

  # Copy local server code
COPY . /code/

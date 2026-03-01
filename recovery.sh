#!/bin/bash

export $(grep -v '^#' .env | xargs)

docker stop $POSTGRES_CONTAINER_NAME
docker rm $POSTGRES_CONTAINER_NAME

sudo rm -rf volume/

docker compose up -d --build
until docker exec $POSTGRES_CONTAINER_NAME pg_isready -U $POSTGRES_USER -d $POSTGRES_DB; do
  echo "waiting for postgres..."
  sleep 0.5
done

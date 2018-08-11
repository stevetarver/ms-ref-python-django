#!/usr/bin/env bash
#
# Run a postgres container for local development
#
docker run -d                       \
    --name postgres                 \
    -p 5432:5432                    \
    -e POSTGRES_PASSWORD=postgres   \
     postgres:10.4-alpine
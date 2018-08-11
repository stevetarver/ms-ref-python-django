#!/usr/bin/env bash
#
# Connect to running postgres container and start psql
#
# Command cheatsheet
#   \?
#   http://www.postgresonline.com/downloads/special_feature/postgresql83_psql_cheatsheet.pdf
#
docker run                  \
    -it --rm                \
    --link postgres:postgres \
    postgres psql -h postgres -U postgres

# Current setup - done once on container create
#    ᐅ ./psql.sh
#    Password for user postgres:
#    psql (10.4 (Debian 10.4-2.pgdg90+1))
#    Type "help" for help.
#
#    postgres=# CREATE DATABASE ms_ref_python_django;
#    CREATE DATABASE
#
# Then, from another shell
#   ./manage.py migrate
# Then
#   ./manage.py runserver
# Then
#   \connect ms_ref_python_django
#   \dt


# Create our test user and database
# Note:
# - currently must be manually pasted into shell
# - currently using postgres user
#CREATE USER test WITH PASSWORD 'test';
#CREATE DATABASE ms_ref_python_django;
#GRANT ALL PRIVILEGES ON DATABASE ms_ref_python_django TO test;

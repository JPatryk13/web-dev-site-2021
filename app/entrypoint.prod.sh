#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Migrate
python manage.py makemigrations --noinput
python manage.py migrate

# Seed database with fake data
python manage.py seed --table Project --entries 4
python manage.py seed --table Link --entries 18

# Create superuser and collect static files
python manage.py createsu
python manage.py collectstatic --noinput

exec "$@"

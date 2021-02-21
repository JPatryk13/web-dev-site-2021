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

# Create superuser and collect static files
python manage.py createsu
python manage.py collectstatic --noinput

exec "$@"

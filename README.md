# webdevsite
Web development services entrepreneurship website. Using: **Docker** via running docker-compose directly on a Linux server.

## Stack:
 - Docker
 - Django (Python)
 - Gunicorn
 - Nginx
 - PostgreSQL

## System:
1. Fedora 32

## Prerequisites:
3. GitHub Account
4. Git CLI
5. Python 3.8
6. Pip
7. Virtualenv
8. Docker 19.03.13

## Steps:

### Project Set-up:

#### Django.

1. Created GitHub repository (with README.md and .gitignore files)
2. Go to *dev* directory and clone the repo
```
$ cd dev
$ git clone <url>
$ cd webdevsite
```
2. Create venv
```
$ virtualenv virt
```
3. Activate it
```
$ source virt/bin/activate
```
4. Install Django
```
$ pip install django==3.1.2
```
It has installed: asgiref-3.2.10 django-3.1.2 pytz-2020.4 sqlparse-0.4.1
5. Start Django project
```
$ django-admin startproject webdevsite .
```
6. Run the app and open *localhost:8000* in the browser
```
$ python manage.py runserver
```
It works now, though, returns `"GET /favicon.ico HTTP/1.1" 404 1976`. Meaning, it cannot find the website icon. I didn't upload any yet so it's not too concerning.
7. Update .gitignore file for Django. Go to https://gist.github.com/santoshpurbey/6f982faf1eacdac153ffd86a3a694239 and copy the file.
8. Upload changes to GitHub
```
$ git add *
$ git status
```
.gitignore file appears to be in *Changes to be committed* section, thus,
```
$ git add .gitignore
```
Then,
```
$ git commit -m "Initial commit"
$ git push
```
9. Go to GitHub to check uploaded files
10. Run migrations (activate environment if necessary - look step no. 3)
```
$ python manage.py migrate
```

#### Gunicorn.

1. Install Gunicorn
```
$ pip install gunicorn==20.0.4
```
2. Test Gunicorn - go to *localhost:8000*
```
$ gunicorn webdevsite.wsgi:application --bind 0.0.0.0:8000
```

#### Docker.

1. Check if Docker and docker-compose are installed and have appropriate versions (docker: 19.03.13, docker-compose: 1.25.4)
```
$ docker --version
$ docker-compose -- version
```
2. Create simple *Dockerfile* in the project directory
```
.
├── db.sqlite3
├── Dockerfile
├── manage.py
├── README.md
├── virt
└── webdevsite
```
```
# pull official base image
FROM python:3.8.6-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
ADD . /app/
```
* pulls an official python alpine image from docker hub
* creates and sets working directory to */app*
* sets environment variables
  PYTHONDONTWRITEBYTECODE disables .pyc files so that the development environment remains nice and clean.
  PYTHONUNBUFFERED ensures that all the python output is sent straight to terminal.
* installs psycopg2(-binary) dependencies
* updates pip and installs modules specified in requirements.txt file
* copies files from the project directory (*.*) to created *app* directory
3. Install PostgreSQL
```
$ pip install psycopg2-binary
```
4. Create requirements.txt
```
$ pip freeze > requirements.txt
```
5. Check PostgreSQL version
```
$ postgres -V
```
6. Create docker-compose.yml file next to the Dockerfile
```
version: '3.7'

services:
  db:
    image: postgres:12.4-alpine
    volumes:
      - ./postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=webdevsite_dev
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app/
    ports:
      - 8000:8000
    env_file:
      - ./.env.dev
    depends_on:
      - db

volumes:
  postgres_data:
```
* uses two services *db* and *web*
* *db* runs from an alpine image, defines volume for the data and some default environment variables to run the database locally
* *web* builds from the current (project) directory and runs the server. Defines the port to be used, environment variables file and dependence
7. Create *.env.dev* file next to docker-compose.yml
```
DEBUG=1
SECRET_KEY=<secret key from the settings file>
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=webdevsite_dev
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db
SQL_PORT=5432
```
8. Update settings.py
```
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", default=0))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
```
...
```
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('SQL_DATABASE', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('SQL_USER', 'user'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'password'),
        'HOST': os.environ.get('SQL_HOST', 'localhost'),
        'PORT': os.environ.get('SQL_PORT', 5432),
    }
}
```
9. Spin up containers
```
$ sudo docker-compose up -d --build
```
10. Run migrations
```
$ sudo docker-compose exec web python manage.py migrate --noinput
```
11. Check if the default Django tables were created
```
$ sudo docker-compose exec db psql --username=postgres --dbname=webdevsite_dev
```
Run `# \l` to see if *webdevsite_dev* exists. Connect to it using `# \c webdevsite_dev` and list tables with `# \dt`. If everything is on its place quit via `# \q`.
12. Check if the volume was created
```
$ docker volume inspect webdevsite_postgres_data
```
Expected output:
```
[
    {
        "CreatedAt": "2020-11-18T13:35:10Z",
        "Driver": "local",
        "Labels": {
            "com.docker.compose.project": "webdevsite",
            "com.docker.compose.version": "1.25.4",
            "com.docker.compose.volume": "postgres_data"
        },
        "Mountpoint": "/var/lib/docker/volumes/webdevsite_postgres_data/_data",
        "Name": "webdevsite_postgres_data",
        "Options": null,
        "Scope": "local"
    }
]
```
13. Create a shell script *entrypoint.sh* next to the Dockerfile - it will check if the database is running and if it does it flushes the database and runs migrations.
```
#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"
```
* Add `DATABASE=postgres` to the *.env.dev* file
* Update Dockerfile
```
# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
```
* Update permissions `$ chmod +x entrypoint.sh`


## Errors
1. Permissions
```
$ docker-compose up -d --build
...
PermissionError: [Errno 13] Permission denied: '/home/patryk/dev/webdevsite/postgres_data'
```
Workaround: use `sudo`, e.g. `$ sudo docker-compose up -d --build` or `$ sudo docker-compose exec web ...`
2. No container found
```
$ sudo docker-compose exec web python manage.py migrate --noinput
...
ERROR: No container found for web_1
```
Solution:
```
$ docker ps -a

CONTAINER ID        IMAGE                  COMMAND                  CREATED              STATUS                          PORTS               NAMES
b56fe7b76c5a        webdevsite_web         "python manage.py ru…"   About a minute ago   Exited (1) About a minute ago                       webdevsite_web_1
311abd837864        postgres:12.4-alpine   "docker-entrypoint.s…"   About a minute ago   Up About a minute               5432/tcp            webdevsite_db_1

$ docker logs b56fe7b76c5a

File "/app/webdevsite/settings.py", line 83
  'PORT': os.environ.get('SQL_PORT', '5432"),
                                            ^
```
in *settings.py* add `import os` and remove confused quotient marks.
3. No database with the name
```
$ sudo docker-compose exec web python manage.py migrate --noinput

django.db.utils.OperationalError: FATAL:  database "webdevsite_dev" does not exist
```
Solution:
```
$ docker ps -a
...
$ docker logs 8c9a870c6a70

PostgreSQL Database directory appears to contain a database; Skipping initialization

$ tree -L 1

.
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── postgres_data
├── README.md
├── requirements.txt
├── virt
└── webdevsite

$ cd postgres_data

bash: cd: postgres_data: Permission denied

$ sudo rm -rf postgres_data
```

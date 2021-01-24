# webdevsite
Web development services entrepreneurship website. Using: **Docker** via running docker-compose directly on a Linux server.

**PLAN 1.09**
- [x] Base project
  - [x] Create GitHub repo and clone it
  - [x] Define prerequisites, stack and plan
  - [x] Set up virtual environment
  - [x] Set up basic Django project and test it
- [x] Development Set-up (Dockerize Django, PostgreSQL)
  - [x] Test if Docker is working
  - [x] Create Dockerfile for development environment
  - [x] Install postgresql
  - [x] Create docker-compose file for development
  - [x] Create .env file for development
  - [x] Update settings file
  - [x] Test database
  - [x] Create entrypoint file for development
- [x] Production Set-up (Gunicorn, Nginx)
  - [x] Install Gunicorn
  - [x] Create Dockerfile.prod
  - [x] Create docker-compose.prod.yml
  - [x] Create .env.prod and .env.prod.db
  - [x] Create entrypoint.prod.sh
  - [x] Set up Nginx
- [x] Static/Media Files and Super User
  - [x] Create an app and add it to INSTALLED_APPS
  - [x] Create a custom management command for creating a super user with pre-defined input
  - [x] Generate superuser credentials and add it to the .env.prod file
  - [x] Add management commands to the entrypoint files for development and production
  - [x] Add static and media files volumes in the docker-compose.prod.yml
  - [x] Update Dockerfile.prod for creating appropriate directory structure withing the container
  - [x] Update nginx.conf for static and media files directories
  - [x] update settings file for media/static files
  - [x] Create a view that serves for saving media files
  - [x] Create a template that allows for saving images
  - [x] Update urls.py so it allows for accessing the view and serves media files in development
- [x] Back-end (Models, Views, Templates)
  - [x] Create models for table Project and Link and register it in admin.py
  - [x] Set LANGUAGE_CODE to en-gb and TIME_ZONE to Europe/London in settings.py
  - [x] Create urls.py in website directory and hook up url mapper so that it still works
  - [x] Define and create URL structure
  - [x] Use decorators (class orientation) to register models in admin.py
  - [x] Create base views (functions/classes) - redirecting
  - [x] Create templates for each page (inc. navbar and footbar partials, base and image upload templates)
    - [x] File structure
    - [x] HTML boiler template
    - [x] Referencing using Django templating language
  - [x] Test integration and correct for potential errors
  - [x] Create 2 or 3 dummy projects
  - [x] Customise index view to return project list
  - [x] Customise index page to display project list
  - [x] Create Hire and Contact forms
  - [x] Customise views to process interaction with forms (development mode, data shall be outputted to the console)
    - [x] Index view - display form and the list of projects
    - [x] Hire me view - display form
  - [x] Create a seeder for tables (https://stackoverflow.com/questions/33024510/populate-django-database)
  - [x] Customise templates to display forms
  - [x] Customise image upload view to allow access only for super user
  - [x] Edit admin.py to access image upload page from the admin page
  - [x] Customise project view to return details about a particular project
    - [x] Just project details
    - [x] Project details with links
  - [x] Customise project template to display the project details
  - [x] Find a way of sending emails from your website to your email (no need to apply currently, save it as a reference for the future - Amazon SAS)
  - [x] Figure out why Faker doesn't install automatically
- [x] Back-end (production environment locally, manual test)
  - [x] Test URL mapping
  - [x] Add auto-creating superuser
  - [x] Add automatic seeding database
  - [x] Test admin page
- [x] Tests
  - [x] Read: https://realpython.com/testing-in-django-part-1-best-practices-and-examples
  - [x] Tests for models
  - [x] Tests for views
  - [x] Tests for forms
- [ ] Front-end (HTML, CSS, JS; Bulma, Sass)
  - [x] Read how to use Bulma
  - [x] Read how to use Sass
  - [ ] Rebuild current templates using Bulma (no need for assets from the design)
  - [ ] Test how to make assets move (JS exercise)
  - [x] Get assets
  - [ ] Create section bookmarks with links
  - [ ] Structure templates using Bulma
  - [ ] Define colours, fonts and sizes
  - [ ] Apply minor changes to a template and test if it works
  - [ ] Export assets from the .xd file
  - [ ] Create profiles on social media to get links
  - [ ] Front-end of the Index page (with dummy text)
    - [ ] Ensure it displays appropriate message when the project section is empty
    - [ ] Create a mobile version
  - [ ] Customise navbar and footbar partials
    - [ ] Create a mobile version
  - [ ] Front-end of the Project page (with dummy text)
    - [ ] Create a mobile version
  - [ ] Front-end of the Hire Me page (with dummy text)
    - [ ] Create a mobile version
  - [ ] Front-end of the Upload page
  - [ ] Create copy (text content of the website, not including projects)
- [ ] Deployment
  - [ ] Ensure server/cloud allows for using Docker
  - [ ] Ensure you have a domain
  - [ ] Deploy files to the server
  - [ ] Get SSL certificate
  - [ ] Test the website for public access from multiple devices through https protocol
- [ ] Extra
  - [ ] Create Error views and basic templates (https://docs.djangoproject.com/en/3.1/ref/views/)

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

#### Docker and PostgreSQL.

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
14. Rebuild Docker container
```
$ docker-compose down -v
$ sudo docker-compose up -d --build
```
15. Go to *localhost:8000* to check if everything is running
16. Upload changes to GitHub
```
$ git add *
$ git status
...
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .env.dev
$ git add .env.dev
$ git commit -m "Webdevsite is now running locally on Docker with PostgreSQL"
$ git push
```

#### Gunicorn (2).

1. Ensure that `gunicorn==20.0.4` is in the *requirements.txt*
2. Create a *docker-compose.prod.yml* file
```
version: '3.7'

services:
  web:
    build: .
    command: gunicorn webdevsite.wsgi:application --bind 0.0.0.0:8000
    ports:
      - 8000:8000
    env_file:
      - ./.env.prod
    depends_on:
      - db
  db:
    image: postgres:12.0-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    env_file:
      - ./.env.prod.db

volumes:
  postgres_data:
```
Changes compared to the *docker-compose.yml*
* `command`: Running server from `gunicorn` rather than `python manage.py`
* `volumes`: Not created for `web` service in production environment
* different `env_file`
* environment variables stored in a `.env.prod.db` file for production
3. Generate `SECRET_KEY`
```
$ source virt/bin/activate
$ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
4. Generate `SQL_PASSWORD`
```
$ python -c 'from django.utils.crypto import get_random_string; print(get_random_string(length=32))'
```
5. Create *.env.prod*
```
DEBUG=0
SECRET_KEY= ...
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=webdevsite_prod
SQL_USER= ...
SQL_PASSWORD= ...
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```
6. Create *.env.prod.db*
```
POSTGRES_USER= ...
POSTGRES_PASSWORD= ...
POSTGRES_DB=webdevsite_prod
```
7. Check *.gitignore*
* add *.env.prod* and *.env.prod.db*
* remove *.env.dev* if exists
8. Rebuild containers
```
$ docker-compose down -v
$ sudo docker-compose -f docker-compose.prod.yml up -d --build
```
*If the container fails to start, check for errors in the logs via* `$ sudo docker-compose -f docker-compose.prod.yml logs -f`.
9. Check if containers are running
```
$ docker ps -a
```
10. Check if the database *webdevsite_prod* was created.
```
$ sudo docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
$ sudo docker-compose -f docker-compose.prod.yml exec db psql --username=patryk --dbname=webdevsite_prod
...
# \l
...
# \c webdevsite_prod
...
# \dt
...
# \q
```

#### Production Docker.

1. Create *entrypoint.prod.sh*
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

exec "$@"
```
It skips flushing the database and automatic migrations.
* Update permissions
```
$ chmod +x entrypoint.prod.sh
```
2. Create a *Dockerfile.prod*
```
###########
# BUILDER #
###########

# pull official base image
FROM python:3.8.6-alpine AS builder

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# lint
RUN pip install --upgrade pip
RUN pip install flake8
COPY . .
RUN flake8 --ignore=E501,F401 --exclude=virt/ .

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.8.6-alpine

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint-prod.sh
COPY ./entrypoint.prod.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.prod.sh
ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]
```
* It uses multi-stage build. The builder stage creates an image necessary to set up an environment for the project and installs packages. The final stage is running the container.
* flake8 is a module that examines the code against the coding convention PEP8 (lint software). It doesn't work well with virtual environment files so they are excluded
* Then packages are installed. `--no-cache-dir` - doesn't store installed modules in cache (reducing image size), `--no-deps` - don't install package dependencies, `--wheel-dir /app/wheels` - stores wheels (build packages) in the directory specified
* Final stage creates a directory and uses *wheels* and *requirements.txt* to install packages.
* Then copies files and switches to the *app* user.
3. Update *docker-compose.prod.yml*
```
build:
  context: .
  dockerfile: Dockerfile.prod
```
4. Restart the container and run migrations
```
$ docker-compose -f docker-compose.prod.yml down -v
$ sudo docker-compose -f docker-compose.prod.yml up -d --build
$ sudo docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```
5. Upload changes to GitHub
```
$ git add *
$ git status
$ git add .gitignore
$ git commit -m "Running Docker in production mode"
$ git push
```

#### Clean up directory structure.

Ensuring that Django project and Dockerfiles have separate directory reduces mess significantly, thus, reducing potential errors arising from confusion.
1. Create *app* folder in the main directory
2. Move *webdevsite*, *manage.py*, entrypoints, *requirements.txt* and Dockerfiles into the *app* directory.
3. Update *docker-compose.yml*
```
[5]   build: ./app
[8]   - ./app/:/app/
```
4. Restart the container to see if it works
```
$ docker-compose -f docker-compose.prod.yml down -v
$ sudo docker-compose up -d --build
$ sudo docker-compose exec web python manage.py migrate --noinput
```
5. Update *docker-compose.prod.yml*
```
[6]   context: ./app
```
6. Restart the container to see if it works
```
$ docker-compose down -v
$ sudo docker-compose -f docker-compose.prod.yml up -d --build
$ sudo docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```
7. Spin it down and upload changes to github
```
$ docker-compose -f docker-compose.prod.yml down -v
$ git add *
$ git status
$ git commit -m "Rearranged directory structure"
$ git push
```

#### Nginx.

1. Update *docker-compose.prod.yml* by adding nginx service
```
nginx:
  build: ./nginx
  ports:
    - 1337:80
  depends_on:
    - web
```
2. Also in the *docker-compose.prod.yml* file, expose (for internal connections) port 8000
```
[9]   expose:
[10]    - 8000
```
3. Create the following dir structure
```
nginx
 ├── Dockerfile
 └── nginx.conf
```
4. *Dockerfile*
```
FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
```
5. *nginx.conf*
```
upstream webdevsite {
    server web:8000;
}

server {

    listen 80;

    location / {
        proxy_pass http://webdevsite;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }

}
```
6. Test if it works
```
$ sudo docker-compose -f docker-compose.prod.yml up -d --build
$ sudo docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```

#### Static Files.

1. Run `$ docker-compose -f docker-compose.prod.yml down -v`
2. Update *settings.py*
```
STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```
3. Run the container in development and open *localhost:8000/admin* to check if static files are served correctly
```
$ sudo docker-compose up -d --build
```
4. For production, add `static_volume` in *docker-compose.prod.yml* in services `web` and `nginx`.
```
volumes:
  - static_volume:/home/app/web/staticfiles
```
Add `static_volume:` in `volumes:`
5. Add `RUN mkdir $APP_HOME/staticfiles` in *Dockerfile.prod*
```
# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME
```
6. Update *nginx.conf* by adding:
```
location /staticfiles/ {
    alias /home/app/web/staticfiles/;
}
```
7. Test - go to *localhost:1337/admin*
```
$ docker-compose down -v
$ sudo docker-compose -f docker-compose.prod.yml up -d --build
$ sudo docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
...
$ docker-compose -f docker-compose.prod.yml down -v
```
8. Upload changes to GitHub

#### In-container directory structure for production.

1. In *Dockerfile.prod*
```
[9]   WORKDIR /usr/src/app
[27]  RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt
[52]  COPY --from=builder /usr/src/app/wheels /wheels
[53]  COPY --from=builder /usr/src/app/requirements.txt .
```
2. Run `$ sudo docker-compose -f docker-compose.prod.yml up -d --build` and `$ sudo docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear` and go to *localhost:1337/admin*

#### Backend (part 1).
1. Create an app
```
$ docker-compose -f docker-compose.prod.yml down -v
$ sudo docker-compose up -d --build
$ sudo docker-compose exec web python manage.py startapp website
```
2. In *settings.py* add the app to `INSTALLED_APPS`.
3. Change owner of the *website* app
```
$ sudo chwon -R $USER ./app/website
```
4. Create models `Project()` and `Link()`
5. Register models in *admin.py*
6. Add *Pillow==8.0.1* to *requirements.txt*
7. Add Pillow dependencies to *Dockerfile* and *Dockerfile.prod*
```
# install Pillow dependencies
RUN apk --no-cache add jpeg-dev \
        zlib-dev \
        freetype-dev \
        lcms2-dev \
        openjpeg-dev \
        tiff-dev \
        tk-dev \
        tcl-dev \
        harfbuzz-dev \
        fribidi-dev
```
6. Restart the container, run migrations and create super user
```
$ docker-compose down -v && sudo docker-compose up -d --build
$ sudo docker-compose exec web python manage.py makemigrations
$ sudo docker-compose exec web python manage.py migrate --noinput
$ sudo docker-compose exec web python manage.py createsuperuser
$ docker-compose down -v
```

#### Create Superuser (dev).

1. In the *website* app directory, create *createsu.py* file at *management/commands*
```
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username=os.environ['SU_NAME']).exists():
            User.objects.create_superuser(os.environ['SU_NAME'], os.environ['SU_EMAIL'], os.environ['SU_PASSWORD'])
```
2. In *.env.dev* add `SU_NAME`, `SU_EMAIL`, `SU_PASSWORD`
3. Add `python manage.py createsu` to the *entrypoint.sh*
4. Run `$ sudo docker-compose up -d --build`
5. Go to *localhost:8000/admin* and log in
6. Spin down containers, `$ docker-compose down -v`
7. Upload changes to GitHub

#### Media Files (dev).

1. Update *settings.py* (add it on the bottom)
```
MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")
```
2. Run `$ sudo docker-compose up -d --build`
7. Go to *localhost:8000/admin*, log in with *SU_NAME* and *SU_PASSWORD* and add a project (https://www.lipsum.com/).
8. Check if the file exists
```
$ docker ps
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS                    NAMES
5c479264ca84        webdevsite_web         "/app/entrypoint.sh …"   5 minutes ago       Up 5 minutes        0.0.0.0:8000->8000/tcp   webdevsite_web_1
47e23b94e902        postgres:12.4-alpine   "docker-entrypoint.s…"   5 minutes ago       Up 5 minutes        5432/tcp                 webdevsite_db_1
$ docker exec -it 5c479264ca84 /bin/sh
/app # ls
Dockerfile          entrypoint.sh       projects            website
Dockerfile.prod     manage.py           requirements.txt
entrypoint.prod.sh  mediafiles          webdevsite
/app # cd mediafiles
/app/mediafiles # cd projects
/app/mediafiles/projects # ls
Slide1.JPG
```

#### Create Superuser (prod)

1. Generate random `SU_PASSWORD` and `SU_NAME` prefix
```
$ python -c 'from django.utils.crypto import get_random_string; print(get_random_string(length=32))'
$ python -c 'from django.utils.crypto import get_random_string; print(get_random_string(length=8))'
```
2. In *.env.prod* add `SU_NAME`, `SU_EMAIL`, `SU_PASSWORD`
3. Add `python manage.py createsu` to the *entrypoint.prod.sh*

#### Media Files (prod).

1. Add `- media_volume:/home/app/web/mediafiles` in *web* and *nginx* services and add `media_volume:` in *volumes*
2. Update *Dockerfile.prod*
```
...
# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME
...
```
3. Update *nginx.conf*
```
...
location /mediafiles/ {
    alias /home/app/web/mediafiles/;
}
...
```
4. Add `python manage.py makemigrations` and `python manage.py migrate --noinput` to *entrypoint.prod.sh*
5. Rebuild the container
```
$ docker-compose down -v
$ sudo docker-compose -f docker-compose.prod.yml up -d --build
$ sudo docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
...
```


**MAJOR ERROR: COULD NOT MAKE PILLOW WORK IN PRODUCTION ENVIRONMENT**
- See *ERROR #8* for more
- Plan: restructure the Project table to save URLs for images instead of using ImageField, remove Pillow, create view and urls structure appropriate for testing, create template appropriate for testing, deploy the app and try uploading an image. Later the view and template will look entirely different to make adding images accessible only from superuser account and to incorporate the table. It can be a ground for administration panel.

#### Backend - inc. media files (part 2).
1. Replace *ImageField* with *URLField* in *models.py*
```
[25]  img = models.URLField(max_length=1000)
```
2. Create view for the image upload
```
# https://docs.djangoproject.com/en/3.1/topics/http/views/

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def upload(request):
    # If the page was previously open and the image is being uploaded the code beneath
    # if is executed. Else, only the return render() and the very end is executed; i.e. empty page is loaded.
    if request.method == "POST" and request.FILES["image_file"]:
        # If the method in the request was POST get the image that is to be uploaded
        image_file = request.FILES["image_file"]

        # https://docs.djangoproject.com/en/3.1/ref/files/storage/#the-filesystemstorage-class
        fs = FileSystemStorage()
        # Get the image url (where it is going to be saved) and print it
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)

        # Save the image at the generated url
        return render(request, "upload.html", {
            "image_url": image_url
        })
    # Else: display the upload page
    return render(request, "upload.html")
```
3. Create a template in *website/templates* for the image upload
```
{% block content %}

  <form action="{% url "upload" %}" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="file" name="image_file">
    <input type="submit" value="submit" />
  </form>

  {% if image_url %}
    <p>File uploaded at: <a href="{{ image_url }}">{{ image_url }}</a></p>
  {% endif %}

{% endblock %}
```
4. Edit *webdevsite/urls.py*
```
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from website.views import image_upload

urlpatterns = [
    # Temporary direct url to the upload view in the website app
    path("", image_upload, name="upload"),
    path('admin/', admin.site.urls),
]

# Uses local storage for media files in development
if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
5. Remove *Pillow* deps from *Dockerfile*
6. Run `$ sudo docker-compose up -d --build` and go to *localhost:8000*
7. Remove *Pillow* deps from *Dockerfile.prod*
8. Run `$ docker-compose down -v && sudo docker-compose -f docker-compose.prod.yml up -d --build` and go to *localhost:1337*
9. Make sure that management commands are included in *entrypoint.sh*
```
[14]  python manage.py flush --no-input
[15]  python manage.py makemigrations --noinput
[16]  python manage.py migrate
[17]  python manage.py createsu
[18]  python manage.py collectstatic --noinput
```
10. Make sure that management commands are included in *entrypoint.prod.sh*
```
[14]  python manage.py makemigrations --noinput
[15]  python manage.py migrate
[16]  python manage.py createsu
[17]  python manage.py collectstatic --noinput
```
11. Re-run development environment
```
$ docker-compose -f docker-compose.prod.yml down -v
$ sudo docker-compose up -d --build
```
12. Check if the container was run without errors
```
$ docker ps
$ docker logs <CONTAINER ID>
```
13. Go to *localhost:8000*, upload an image and click the link to see if was correctly uploaded
14. Spin up production container
```
$ docker-compose down -v
$ sudo docker-compose -f docker-compose.prod.yml up -d --build
```

#### Back-end (Models, Views, Templates) (Part 3).
1. Changed *CharField* for *status* to *BooleanField* for *public* in *website/models.py*
2. Customised *LANGUAGE_CODE* and *TIME_ZONE* in *settings.py*
3. Customised *webdevsite/urls.py* so it maps to *website/urls.py*
```
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('website.urls')),
    path('admin/', admin.site.urls),
]
...
```
4. Created *website/urls.py*
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('hire-me/', views.hire_me, name='hire-me'),
    path('upload/', views.upload, name='upload'),
]
```
5. Re-register models in *admin.py* using decorators
```
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass
```
6. Create plane views
```
...
from django.views import generic

class Index(generic.ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'index.html'


class ProjectDetailView(generic.DetailView):
    model = Project


def hire_me(request):
    return render(request, 'hire-me.html')
...
```
7. Create templates
```
.
├── base.html
├── hire-me.html
├── index.html
├── partials
│   ├── footbar.html
│   └── navbar.html
├── project-detail.html
└── upload.html
```
8. In files *hire-me*, *index* added words indicating name of the file. E.g. I put `hire-me` in *hire-me.html* file.
9. Run container and go to *localhost:8000* and *localhost:8000/hire-me*
10. Create base template and add some text to it as well as to the *footbar* and *navbar* files.
11. Go to *localhost:8000* and *localhost:8000/hire-me* again to test.
12. Get a base HTML template, upload put it in *base.html* and reference `navbar`, `content`, `footbar` blocks using Django templating language
```
...
<body>
  {% block navbar %}{% include "partials/navbar.html" %}{% endblock %}

  template

  {% block content %}that part should be replaced{% endblock %}

  {% block footbar %}{% include "partials/footbar.html" %}{% endblock %}
</body>
...
```
13. Build a code in *index.html* that displays list of the projects
```
{% extends "base.html" %}

{% block content %}
<h1>Projects</h1>
  {% if project_list %}
  <ul>
    {% for project in project_list %}
      <li>
        <img src="{{ project.img }}" alt="{{ project.title }}" width="10%" height="10%">
        <a href="{{ project.get_absolute_url }}">{{ project.title }}</a> {{ project.date_finished }}
        <p>
          {{ project.prev_description }}
        </p>
      </li>
    {% endfor %}
  </ul>
  {% else %}
    <p>There is no projects that has been finished.</p>
  {% endif %}
{% endblock %}
```
14. Add a date-time field and ordering Meta in the models file
```
...
date_finished = models.DateTimeField(
      verbose_name='Date.',
      help_text='When the project has been finished.'
  )
...
  class Meta:
      ordering = ['date_finished']
...
```
15. Spin up containers if they are not up, go to *localhost:8000/upload* and upload two arbitrary images (copy links, we will need them)
16. Go to *localhost:8000/admin* and add two dummy projects - use copied links to reference images
17. Two changes to be made; `verbose_name` in `date_finished` to `Date finished.` and `help_text` in `public` to `Check if you want the project to be public.`. Also change `DateTimeField` type for `date_finished` to `DateField` + **Error #10**
```
...
date_finished = models.DateField(
      default=None,
      null=True,
      verbose_name='Date finished.',
      help_text='When the project has been finished.'
  )
...
public = models.BooleanField(default=False, help_text='Check if you want the project to be public.')
...
```
18. As soon as projects are successfully added go to the main page to verify if the projects are listed properly
19. Create class-based *forms.py*
20. Create Views serving forms
21. Change some functions into classes in *views.py*
22. Update URLs
23. Update *settings.py* for email backends
24. Customise *hire-me.html* and *index.html* templates so they both display forms
25. Bring back listing projects in the *index.html* template
26. Install *faker*; in virtual environment `$ pip install Faker`
27. Create *seed.py* in *management/commands/*
28. Add default value for the image url in the Project model
```
img = models.URLField(
    max_length=1000,
    verbose_name='Image.',
    help_text='URL to an image that will appear in the home page.',
    default='https://i.ytimg.com/vi/E9U9xS4thxU/hqdefault.jpg' # temporarily, eases using faker
)
```
29. Seed database `$ docker-compose exec web python manage.py seed`
30. Add verification for superuser in the upload view
```
# Verify if the user has superuser permissions
  if not request.user.is_superuser:
      raise PermissionDenied()
```
31. Update settings so they are able to discover custom admin templates
```
[59]  'DIRS': [os.path.join(BASE_DIR, "website/templates")],
```
33. Go to `/home/patryk/dev/webdevsite/virt/lib/python3.8/site-packages/django/contrib/admin/templates` - django admin templates directory. Display the content:
```
.
├── admin
│   ├── 404.html
│   ├── 500.html
│   ├── actions.html
│   ├── app_index.html
│   ├── app_list.html
│   ├── auth
│   │   └── user
│   │       ├── add_form.html
│   │       └── change_password.html
│   ├── base.html
│   ├── base_site.html
│   ├── change_form.html
│   ├── change_form_object_tools.html
│   ├── change_list.html
│   ├── change_list_object_tools.html
│   ├── change_list_results.html
│   ├── date_hierarchy.html
│   ├── delete_confirmation.html
│   ├── delete_selected_confirmation.html
│   ├── edit_inline
│   │   ├── stacked.html
│   │   └── tabular.html
│   ├── filter.html
│   ├── includes
│   │   ├── fieldset.html
│   │   └── object_delete_summary.html
│   ├── index.html
│   ├── invalid_setup.html
│   ├── login.html
│   ├── nav_sidebar.html
│   ├── object_history.html
│   ├── pagination.html
│   ├── popup_response.html
│   ├── prepopulated_fields_js.html
│   ├── search_form.html
│   ├── submit_line.html
│   └── widgets
│       ├── clearable_file_input.html
│       ├── foreign_key_raw_id.html
│       ├── many_to_many_raw_id.html
│       ├── radio.html
│       ├── related_widget_wrapper.html
│       ├── split_datetime.html
│       └── url.html
└── registration
    ├── logged_out.html
    ├── password_change_done.html
    ├── password_change_form.html
    ├── password_reset_complete.html
    ├── password_reset_confirm.html
    ├── password_reset_done.html
    ├── password_reset_email.html
    └── password_reset_form.html
```
32. Create a directory structure and a file *templates/admin/app_list.html*
33. Copy the code from *app_list.html* (in *.../django/contrib/admin/templates/*) to the new created file
34. Update the code so it includes a link to the upload page
```
[37]   {% endfor %}
[38]    <a href="{% url 'upload' %}">Upload an image.</a>
[39]  {% else %}
```
35. Add `template_name = 'project-detail.html'` in `ProjectDetailView` in *views.py*
36. Build a basic detail view for the project
37. Create and test seeder for the Link table
38. Customise ProjectDetailView so it return both a project and a list of Links related to it

## **Done with the step-by-step guide. Updated only in the case of significant changes and errors.**

## Useful commands:
1. Running test and generating coverage reports
```
$ docker-compose exec web coverage run manage.py test -v 2
$ docker-compose exec web coverage html
```
2. Cleaning up docker
* List all images and stuff dangling around in docker: `$ docker images --format 'table {{.Repository}}\t{{.Tag}}\t{{.ID}}\t{{.CreatedAt}}\t{{.Size}}'`
* Remove images created before the date 'until': `$ docker image prune -a --force --filter "until=2020-11-20T14:22:53"`
* Remove all data associated with docker: `$ docker system prune --volumes`
3. Dealing with SCSS - **I'm currently using DIY sass-compiler.py module**
* Compile SCSS on the go: `$ docker-compose exec web python manage.py sass website/static/scss/ website/static/css/ --watch` (you can remove `docker-compose exec web` part and add it to the entrypoint file).
* Compile SCSS manually: `$ docker-compose exec web python manage.py sass website/static/scss/ website/static/css/`
In production add that to the entrypoint file before collectstatic command: `python manage.py sass website/static/scss/ website/static/css/ -t compressed`
4. Enter the container's cmd : `$ docker exec -it <container ID> /bin/sh`







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
4. Messed up directories
```
$ sudo docker-compose -f docker-compose.prod.yml up -d --build
...
Step 20/27 : COPY --from=builder ./wheels /wheels
ERROR: Service 'web' failed to build: COPY failed: stat /var/lib/docker/overlay2/e2b1fc7c000f161443678ce03fe39a9274e4cabfc531870b494664d63955b2b2/merged/wheels: no such file or directory
```
Have: `RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt`, `COPY --from=builder ./wheels /wheels`
Update:
```
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
```
5. Missing dependencies for Pillow
```
& sudo docker-compose up -d --build
...
Traceback (most recent call last):                                              
  File "<string>", line 1, in <module>                                          
  File "/tmp/pip-install-ix6mw5a4/pillow/setup.py", line 914, in <module>       
    raise RequiredDependencyException(msg)                                      
__main__.RequiredDependencyException:                                           

The headers or library files could not be found for zlib,                       
a required dependency when compiling Pillow from source.
```
Solution: add Pillow dependencies to Dockerfile
```
# install Pillow dependencies
RUN apk --no-cache add jpeg-dev \
        zlib-dev \
        freetype-dev \
        lcms2-dev \
        openjpeg-dev \
        tiff-dev \
        tk-dev \
        tcl-dev \
        harfbuzz-dev \
        fribidi-dev
```
6. Running createsu custom management command
```
@Dockerfile
...
# copy project
COPY . .

# create super user
RUN python manage.py createsu

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
```
```
$ sudo docker-compose up -d --build
...
File "/app/webdevsite/settings.py", line 29, in <module>                        
    ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(' ')             
AttributeError: 'NoneType' object has no attribute 'split'                        
ERROR: Service 'web' failed to build: The command '/bin/sh -c python manage.py createsu' returned a non-zero code: 1
```
Solution: add `python manage.py createsu` to the *entrypoint.sh*
7. Missing *reverse* library in *models.py*
```
$ sudo docker-compose -f docker-compose.prod.yml up -d --build
...
Step 9/28 : RUN flake8 --ignore=E501,F401 --exclude=virt/ .
 ---> Running in ef16826fea69
./website/models.py:44:16: F821 undefined name 'reverse'
```
Solution: add `from django.urls import reverse` to *models.py*
8. Migrating failed on ImageField (Pillow)
```
$ sudo docker-compose -f docker-compose.prod.yml exec app python manage.py migrate --noinput
...
Cannot use ImageField because Pillow is not installed.
    HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
```
Solution (attempt 1): add `python manage.py makemigrations` and `python manage.py migrate --noinput` to *entrypoint.prod.sh*
Result: Containers sucessfully built, although, the error persists when trying to open *localhost:1337/admin* (*Server Error (500)*)
Solution: Add another dependencies for Pillow in *Dockerfile* and *Dockerfile.prod*
```
...
# install Pillow dependencies
RUN apk --no-cache add jpeg-dev \
        zlib-dev \
        freetype-dev \
        lcms2-dev \
        openjpeg-dev \
        tiff-dev \
        tk-dev \
        tcl-dev \
        harfbuzz-dev \
        fribidi-dev \
        libjpeg \
        libpq
...
```
Result: Running `$ sudo docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput` results in the same error
* Test different versions of Pillow (6.2.1, 6.2.2, 7.0.0, 7.1.0, 7.1.1, 7.1.2, 7.2.0, 8.0.0, 8.0.1) (running `$ docker-compose -f docker-compose.prod.yml down -v && sudo docker-compose -f docker-compose.prod.yml up -d --build && sudo docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput` after each change). Versions failed: 8.0.1, 8.0.0, 7.2.0, 7.1.2, 7.1.1, 7.1.0.
* Trying slim-buster
* Trying different version of python
* Trying different set of dependencies
* Trying old directory structure
* Trying to install it not from wheels
* Trying single-stage build
9. Failing to create *db* container
```
$ sudo docker-compose -f docker-compose.prod.yml up -d --build
$ docker ps -a
CONTAINER ID        IMAGE                  COMMAND                  CREATED              STATUS                          PORTS                  NAMES
02eeea4de593        webdevsite_nginx       "/docker-entrypoint.…"   58 seconds ago       Up 55 seconds                   0.0.0.0:1337->80/tcp   webdevsite_nginx_1
00efcbbb763f        webdevsite_web         "/home/app/web/entry…"   About a minute ago   Up 57 seconds                   8000/tcp               webdevsite_web_1
d5a19826e0a1        postgres:12.0-alpine   "docker-entrypoint.s…"   About a minute ago   Exited (1) About a minute ago                          webdevsite_db_1
$ docker logs d5a19826e0a1
...
fixing permissions on existing directory /var/lib/postgresql/data ... ok
initdb: error: could not create directory "/var/lib/postgresql/data/pg_wal": No space left on device
initdb: removing contents of data directory "/var/lib/postgresql/data"
```
Solution: remove some old images (https://docs.docker.com/engine/reference/commandline/image_prune/)
```
$ docker images --format 'table {{.Repository}}\t{{.Tag}}\t{{.ID}}\t{{.CreatedAt}}\t{{.Size}}'
REPOSITORY          TAG                 IMAGE ID            CREATED AT                      SIZE
webdevsite_web      latest              3545b1c6ebbc        2020-11-20 15:29:41 +0000 GMT   91.5MB
<none>              <none>              f9bd24327c5a        2020-11-20 15:29:11 +0000 GMT   571MB
webdevsite_nginx    latest              b750759402de        2020-11-20 14:22:54 +0000 GMT   21.3MB
<none>              <none>              8b87beff5842        2020-11-20 14:22:52 +0000 GMT   91.5MB
<none>              <none>              e6efbf56ba2e        2020-11-20 14:22:09 +0000 GMT   571MB
...
$ docker image prune -a --force --filter "until=2020-11-20T14:22:53"
```
10. Failed to migrate database after changes
After filling up the form to create a entry in Project table it fails to upload it
```
ProgrammingError at /admin/website/project/add/
column "date_finished" of relation "website_project" does not exist
LINE 1: ...ect" ("title", "prev_description", "description", "date_fini...
                                                             ^
```
* Run `$ docker ps` and `$ docker logs <web container ID>`
```
Waiting for postgres...
PostgreSQL started
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, website
Running migrations:
  No migrations to apply.
  Your models have changes that are not yet reflected in a migration, and so won't be applied.
  Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
```
* Run `$ docker-compose exec web python manage.py makemigrations`
```
You are trying to add a non-nullable field 'date_finished' to project without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option:
```
* Seems like I forgot about the fact that new columns must contain a case to serve for existing rows, i.e. default option.
* Edit the Project model
```
date_finished = models.DateTimeField(
      default=None,
      null=True,
      verbose_name='Date.',
      help_text='When the project has been finished.'
  )
```

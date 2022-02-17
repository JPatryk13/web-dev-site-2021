# Webdevsite
Web-dev services website utilising **Django** framework and **Docker** containers. Single page layout and modern minimal design created using **Bulma**, **Sass** and **JavaScript**. I made it to practise back-end, front-end as well as design. The website runs locally on **Linux Fedora 32** and **Microsoft Windows 10**.

## Stack:
 - Docker
 - Django
 - Gunicorn
 - Nginx
 - PostgreSQL

## Deployed to:
 - AWS
 - Heroku
#### Currently unavailable online.

## System:
1. Fedora 32
2. Windows 10

## Requirements:
1. GitHub Account + GitHub CLI / GitHub Desktop
2. Python 3.8 + Pip
3. Docker 19.03.13

## Major Development and Deployment Steps
1. Base set-up - *define project structure and create virtual repo, virtual environment and base Django project*
2. Development set-up (Dockerize Django, PostgreSQL) - *create Dockerfile and docker-compose for development*
3. Local production set-up (Gunicorn, Nginx) - *create Dockerfile and docker-compose for production, set up Nginx*
4. Static/Media Files and Super User - *create a custom management command for creating a superuser with pre-defined input, update Docker, Django and Nginx to serve static and media files*
5. Back-end (Models, Views, Templates)
6. Back-end (production environment locally, manual test)
7. Automating tests
8. Front-end (HTML, CSS, JS; Bulma, Sass)
9. Deployment to AWS
10. Deployment to Heroku

#### The above roughly covers the process. There has been some changes throughout the development which made the whole process resembling agile development style. 

## Errors & Solutions

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
11. Fixed the error with Pillow... it took me so long. Worth it.

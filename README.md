# webdevsite
Web development services entrepreneurship website. Using: **Docker** via running docker-compose directly on a Linux server.

### Stack:
 - Docker
 - Django (Python)
 - Gunicorn
 - Nginx
 - PostgreSQL

### System:
1. Fedora 32

### Prerequisites:
3. GitHub Account
4. Git CLI
5. Python 3.8
6. Pip
7. Virtualenv
8. Docker 19.03.13

## Steps:

### Project Set-up:

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
$ python manage.py makemigrations
$ python manage.py migrate
```

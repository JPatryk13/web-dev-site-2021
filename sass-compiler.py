import sass
import os

# Input and output directories for Sass and CSS files respectively
input_dir = 'app/website/static/scss/'
output_dir = 'app/website/static/css/'

sass.compile(dirname=(input_dir, output_dir), output_style='compressed')

# Collect static needs to run after compilation to get the file in the
# staticfiles folder. Cannot directly transfer the file to the staticfiles; it
# doesn't work for some reason.
cmd = 'docker-compose exec web python manage.py collectstatic --noinput'
os.system(cmd)

# run: python -m sass-compiler

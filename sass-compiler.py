import sass
import os

# Input and output directories for Sass and CSS files respectively
scss_file_dir = 'app/website/static/scss/style.scss'
css_file_dir = 'app/website/static/css/style.css'

compiled_css_file = sass.compile(filename=scss_file_dir, output_style='compressed')

# Write compiled css to a file
write_file = open(css_file_dir, 'w', encoding="utf-8")
write_file.write(compiled_css_file)

# Collect static needs to run after compilation to get the file in the
# staticfiles folder. Cannot directly transfer the file to the staticfiles; it
# doesn't work for some reason.
cmd = 'docker-compose exec web python manage.py collectstatic --noinput'
os.system(cmd)

# run: python -m sass-compiler

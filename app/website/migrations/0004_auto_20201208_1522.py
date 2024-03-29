# Generated by Django 3.1.2 on 2020-12-08 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20201203_1752'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['date_finished']},
        ),
        migrations.AddField(
            model_name='project',
            name='date_finished',
            field=models.DateField(default=None, help_text='When the project has been finished.', null=True, verbose_name='Date finished.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.URLField(help_text='URL to an image that will appear in the home page.', max_length=1000, verbose_name='Image.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='public',
            field=models.BooleanField(default=False, help_text='Check if you want the project to be public.'),
        ),
    ]

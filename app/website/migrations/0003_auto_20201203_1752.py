# Generated by Django 3.1.2 on 2020-12-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20201202_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='status',
        ),
        migrations.AddField(
            model_name='project',
            name='public',
            field=models.BooleanField(default=False, help_text='Check the False if you want the project to be private.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='prev_description',
            field=models.TextField(help_text='Max: 500 chars.', max_length=200, verbose_name='Short description.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(help_text='Max: 200 chars.', max_length=100, verbose_name='Project title.'),
        ),
    ]

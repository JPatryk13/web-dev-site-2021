# Generated by Django 3.1.2 on 2020-11-19 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Max: 100 chars.', max_length=100, verbose_name='Project title.')),
                ('prev_description', models.TextField(help_text='Max: 200 chars.', max_length=200, verbose_name='Short description.')),
                ('description', models.TextField(help_text='Max: 100000 chars. Use HTML to make it look good.', max_length=100000, verbose_name='Description.')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('img', models.ImageField(upload_to='projects')),
                ('status', models.CharField(blank=True, choices=[('e', 'Edit'), ('p', 'Public')], default='e', help_text='Status of the post.', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_name', models.CharField(help_text='Max: 200 chars.', max_length=200, verbose_name='Name for the link.')),
                ('url', models.URLField(max_length=1000)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.project')),
            ],
        ),
    ]

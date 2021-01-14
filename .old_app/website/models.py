from django.db import models
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Project title.',
        help_text='Max: 100 chars.'
    )
    prev_description = models.TextField(
        max_length=500,
        verbose_name='Short description.',
        help_text='Max: 500 chars.'
    )
    description = models.TextField(
        max_length=5000,
        verbose_name='Description.',
        help_text='Max: 5000 chars. Use HTML to make it look good.'
    )

    date_finished = models.DateField(
        default=None,
        null=True,
        verbose_name='Date finished.',
        help_text='When the project has been finished.'
    )

    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    img = models.OneToOneField(
        'Image',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    public = models.BooleanField(default=False, help_text='Check if you want the project to be public.')

    class Meta:
        ordering = ['date_finished']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])


class Link(models.Model):
    url_name = models.CharField(
        max_length=200,
        verbose_name='Name for the link.',
        help_text='Max: 200 chars.'
    )

    url = models.URLField(max_length=1000)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.url_name

class Image(models.Model):
    # URL to the image
    url =  models.URLField(max_length=1000)
    # Name of the image
    img_name = models.CharField(
        max_length=200,
        help_text='Max: 200 chars.'
    )

    def __str__(self):
        return self.img_name

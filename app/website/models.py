from django.db import models


class Project(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Project title.',
        help_text='Max: 100 chars.'
    )
    prev_description = models.TextField(
        max_length=200,
        verbose_name='Short description.',
        help_text='Max: 200 chars.'
    )
    description = models.TextField(
        max_length=100000,
        verbose_name='Description.',
        help_text='Max: 100000 chars. Use HTML to make it look good.'
    )

    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    img = models.ImageField(upload_to='projects', editable=True)

    # When status set to 'e', the project post won't be public
    STATUS = (
        ('e', 'Edit'),
        ('p', 'Public'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='e',
        help_text='Status of the post.'
    )

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

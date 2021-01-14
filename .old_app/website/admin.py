from django.contrib import admin
from .models import Project, Link, Image


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Project)
# admin.site.register(Link)

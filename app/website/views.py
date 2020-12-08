# https://docs.djangoproject.com/en/3.1/topics/http/views/

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views import generic
from .models import Project

class Index(generic.ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'index.html'


class ProjectDetailView(generic.DetailView):
    model = Project


def hire_me(request):
    return render(request, 'hire-me.html')


def upload(request):
    # If the page was previously open and the image is being uploaded the code beneath
    # if is executed. Else, only the return render() and the very end is executed; i.e. empty page is loaded.
    if request.method == 'POST' and request.FILES['image_file']:
        # If the method in the request was POST get the image that is to be uploaded
        image_file = request.FILES['image_file']

        # https://docs.djangoproject.com/en/3.1/ref/files/storage/#the-filesystemstorage-class
        fs = FileSystemStorage()
        # Get the image url (where it is going to be saved) and print it
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)

        # Save the image at the generated url
        return render(request, 'upload.html', {
            'image_url': image_url
        })
    # Else: display the upload page
    return render(request, 'upload.html')

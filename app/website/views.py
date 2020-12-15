# https://docs.djangoproject.com/en/3.1/topics/http/views/

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views import generic, View
from .models import Project
from .forms import HireMeForm, ContactForm
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.core.exceptions import PermissionDenied

class Index(View):
    template_name = 'index.html'

    project_list = Project.objects.all()

    form_class = ContactForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, { 'form': form, 'project_list': self.project_list })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.send_message()
            return redirect('/contact-success/')



def contact_success(TemplateView):
    return HttpResponse('Success! Thank you for your message.')



class ProjectDetailView(generic.DetailView):
    model = Project



class HireMe(FormView):
    template_name = 'hire-me.html'
    form_class = HireMeForm
    success_url = '/hire-me-success/'

    def form_valid(self, form_class):
        form_class.send_message()
        return super().form_valid(form_class)



def hire_me_success(TemplateView):
    return HttpResponse('Success! Thank you for your message.')



def upload(request):
    # Verify if the user has superuser permissions
    if not request.user.is_superuser:
        raise PermissionDenied()

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

# https://docs.djangoproject.com/en/3.1/topics/http/views/

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views import generic, View
from .models import Project, Link
from .forms import HireMeForm, ContactForm
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.core.exceptions import PermissionDenied


class Index(View):
    """
    template_name - html file name (string) to be rendered,
    project_list - QuerySet of all projects in database,
    form_class - object of the ContactForm class,
    initial - dictionary to structurise the label-input pairs of the form (?),
    form - form object with label-input pairs,
    context - dictionary passed to the render function.
    """

    template_name = 'index.html'

    # Get QuerySet of all objects in Project table. The table is queried only
    # when there is an interaction performed on the QuerySet, i.e. passing it to
    # the context
    project_list = Project.objects.all()

    form_class = ContactForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        # The function creates a context and returns it to the index template
        # with request whenever the request == get

        # return HttpResponse(self.project_list) # Test line to return pure QuerySet
        form = self.form_class(initial=self.initial)
        context = {'form': form, 'project_list': self.project_list}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # The function validates the data passed to the form and returns success
        # message if appropriate

        form = self.form_class(request.POST)

        if form.is_valid():
            form.send_message()
            return redirect('/contact-success/')


def contact_success():
    # temporarily it returns a success message when the contact form is
    # successfully submitted
    return HttpResponse('Success! Thank you for your message.')


class ProjectDetailView(View):
    """
    template_name - html file name (string) to be rendered,
    context - dictionary passed to the render function.
    """

    template_name = 'project-detail.html'

    def get(self, request, *args, **kwargs):
        # When the request is GET, the function fetches project with requested
        # pk and associated links. Then, it passes the data as the context
        # alongside the template and the request to the render function

        context = {
            'project': Project.objects.get(pk=self.kwargs['pk']),
            'links': Link.objects.filter(project_id=self.kwargs['pk'])
        }
        return render(request, self.template_name, context)


class HireMe(FormView):
    """
    template_name - html file name (string) to be rendered,
    form_class - object of the HireMeForm class,
    success_url - url to the success view,
    context - dictionary passed to the render function.

    The class if based on the generic FormView; it renders form (GET request),
    serves input (POST request), validates data and returns success view if the
    data are valid.
    """

    template_name = 'hire-me.html'
    form_class = HireMeForm
    success_url = '/hire-me-success/'

    def form_valid(self, form_class):
        # The function that is run when the form input is valid. It sends a
        # message.

        form_class.send_message()
        return super().form_valid(form_class)


def hire_me_success():
    # temporarily it returns a success message when the hire me form is
    # successfully submitted
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

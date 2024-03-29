# https://docs.djangoproject.com/en/3.1/topics/http/views/

from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Project, Link, Image
from .forms import HireMeForm, ContactForm, UploadImageForm
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
    image_list = Image.objects.all()

    form_class = ContactForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        # The function creates a context and returns it to the index template
        # with request whenever the request == get

        # return HttpResponse(self.project_list) # Test line to return pure QuerySet
        form = self.form_class(initial=self.initial)
        context = {
            'form': form,
            'project_list': self.project_list,
            'image_list': self.image_list
        }
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


class Upload(View):
    """
    template_name - html file name (string) to be rendered,
    form_class - object of the ContactForm class,
    initial - dictionary to structurise the label-input pairs of the form (?)

    Custom upload view. Checks if the superuser permission is granted
    (check_permission), then returns empty form with only one field - image name
    - the upload field is covered by the template. When both are correctly
    entered by superuser, the view extracts image file from the request and the
    form handles the image name. Then the form saves the file's url with given
    name in database and returns those pieces of information to the upload view.
    """

    template_name = 'upload.html'
    form_class = UploadImageForm
    initial = {'key': 'value'}

    def check_permission(self, request):
        # Verify if the user has superuser permissions
        if not request.user.is_superuser:
            raise PermissionDenied()

    def get(self, request, *args, **kwargs):
        self.check_permission(request)

        # Get the empty form
        form = self.form_class(initial=self.initial)
        context = {'form': form}

        # Render the empty form to the upload template
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.check_permission(request)

        # Retrieve image file from request
        image_file = request.FILES['image_file']

        # Get the image name from the form input
        form = self.form_class(request.POST)

        if form.is_valid():
            # Upload image and get the context (image name, url)
            context = form.upload_image(image_file)
            # Render context to the upload template
            return render(request, self.template_name, context)

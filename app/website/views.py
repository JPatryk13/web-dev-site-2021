# https://docs.djangoproject.com/en/3.1/topics/http/views/

from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Project, Link
from .forms import HireMeForm, ContactForm
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
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
        # The function creates the context and returns it to the index template
        # with request whenever the request == get

        # return HttpResponse(self.project_list) # Test line to return pure QuerySet
        form = self.form_class(initial=self.initial)
        context = {
            'form': form,
            'project_list': self.project_list,
            'go_to_contact': False
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # The function validates the data passed to the form and returns success
        # message if appropriate
        form = self.form_class(request.POST)

        if form.is_valid():
            form.send_message()
            context = {
                'project_list': self.project_list,
                'sent': True,
                'go_to_contact': True
            }
            return render(request, self.template_name, context)
        else:
            context = {
                'project_list': self.project_list,
                'sent': False,
                'go_to_contact': True
            }
            return render(request, self.template_name, context)


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


class ProjectDetail(ListView):
    """Detail view using generic list view and pagination"""

    model = Project
    template_name = 'project-detail.html'
    context_object_name = 'projects'
    paginate_by = 1
    queryset = Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProjectDetail, self).get_context_data(**kwargs)
        context['links'] = Link.objects.all()
        return context


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
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.send_message()
            context = {'sent': True}
            return render(request, self.template_name, context)
        else:
            context = {'sent': False}
            return render(request, self.template_name, context)

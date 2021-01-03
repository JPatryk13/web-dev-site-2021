from django import forms
from django.core.mail import send_mail
from datetime import datetime
import os


class HireMeForm(forms.Form):
    # client's name ('name')
    name = forms.CharField(help_text='Name')
    # client's email ('email')
    email = forms.EmailField(help_text='Email')
    # what is your project about? options: web design, back-end, front-end, something else
    TYPES = (
        ('d', 'Web Design'),
        ('b', 'Back End'),
        ('f', 'Front End'),
        ('s', 'Something Else'),
    )
    project_type = forms.ChoiceField(choices=TYPES, label='What is your project about?')
    # is this an existing project or a new one? options: existing, new
    STATUS = (
        ('e', 'Existing'),
        ('n', 'New'),
    )
    project_status = forms.ChoiceField(choices=STATUS, label='Is this an existing project or a new one?')
    # tell me something about your project
    description = forms.CharField(help_text='Tell me something about your project')

    def send_message(self):
        # name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        project_type = self.cleaned_data['project_type']
        project_status = self.cleaned_data['project_status']
        description = self.cleaned_data['description']

        message = 'Project type: ' + project_type + '\n' + 'Project status: ' + project_status + '\n' + description

        send_mail('Hire Me, ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), message, email, [os.environ['SU_EMAIL']])


class ContactForm(forms.Form):
    # Name
    name = forms.CharField(help_text='Name')
    # Email
    email = forms.EmailField(help_text='Email')
    # Message
    message = forms.CharField(help_text='Message')

    def send_message(self):
        send_mail(self.cleaned_data['name'] + ' ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), self.cleaned_data['message'], self.cleaned_data['email'], [os.environ['SU_EMAIL']])

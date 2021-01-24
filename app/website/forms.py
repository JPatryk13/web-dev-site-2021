from django import forms
from django.core.mail import send_mail
from datetime import datetime
from django.core.files.storage import FileSystemStorage
import os


class HireMeForm(forms.Form):
    # client's name ('name')
    name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'John Smith',
                'class': 'input'
            }
        )
    )
    # client's email ('email')
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'johnsmith@domain.com',
                'class': 'input'
            }
        )
    )

    # what is your project about? options: web design, back-end, front-end, something else
    TYPES = (
        ('d', 'Web Design'),
        ('b', 'Back End'),
        ('f', 'Front End'),
        ('s', 'Something Else'),
    )
    project_type = forms.ChoiceField(
        choices=TYPES,
        label='What is your project about?',
        initial='',
        widget=forms.RadioSelect(),
        required=True
    )
    # is this an existing project or a new one? options: existing, new
    STATUS = (
        ('e', 'Existing'),
        ('n', 'New'),
    )
    project_status = forms.ChoiceField(
        choices=STATUS,
        label='Is this an existing project or a new one?',
        initial='',
        widget=forms.RadioSelect(),
        required=True
    )

    # tell me something about your project
    description = forms.CharField(
        label='Project description',
        max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Tell me something about your project',
                'class': 'textarea'
            }
        )
    )

    def clean(self):
        self.name = self.cleaned_data.get('name')
        self.email = self.cleaned_data.get('email')
        self.project_type = self.cleaned_data.get('project_type')
        self.project_status = self.cleaned_data.get('project_status')
        self.description = self.cleaned_data.get('description')

    def send_message(self):
        message = 'Project type: ' + self.project_type + '\n' + 'Project status: ' + self.project_status + '\n' + self.description

        send_mail('Hire Me, ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), message, self.email, [os.environ['SU_EMAIL']])


class ContactForm(forms.Form):
    # Name
    name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'John Smith',
                'class': 'input'
            }
        )
    )
    # Email
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'johnsmith@domain.com',
                'class': 'input'
            }
        )
    )
    # Message
    message = forms.CharField(
        label='Message',
        max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Write your message here',
                'class': 'textarea'
            }
        )
    )

    def clean(self):
        self.name = self.cleaned_data.get('name')
        self.email = self.cleaned_data.get('email')
        self.message = self.cleaned_data.get('message')

    def send_message(self):
        send_mail(self.name + ' ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), self.message, self.email, [os.environ['SU_EMAIL']])

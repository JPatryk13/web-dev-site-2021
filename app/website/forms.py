from django import forms


class HireMeForm(forms.Form):
    # client's name ('name')
    name = forms.CharField(...)
    # client's email ('email')
    email = forms.EmailField(...)
    # what is your project about? options: web design, back-end, front-end, something else
    TYPES = (
        ('d', 'Web Design'),
        ('b', 'Back End'),
        ('f', 'Front End'),
        ('s', 'Something Else'),
    )
    project_type = forms.ChoiceField(choices=TYPES)
    # is this an existing project or a new one? options: existing, new
    STATUS = (
        ('e', 'Existing'),
        ('n', 'New'),
    )
    project_status = forms.ChoiceField(choices=STATUS)
    # tell me something about your project
    description = forms.CharField(...)
    pass


class ContactForm(forms.Form):
    # Name
    name = forms.CharField(...)
    # Email
    email = forms.EmailField(...)
    # Message
    message = forms.CharField(...)
    pass

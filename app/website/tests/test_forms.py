from django.test import TestCase
from faker import Faker
from http import HTTPStatus

from website.forms import HireMeForm, ContactForm

def make_long_string(min_nb_chars=0):
    faker = Faker('en_US')
    long_string = ''

    while len(long_string) < min_nb_chars:
        long_string = faker.text(max_nb_chars=min_nb_chars*2)

    return long_string


class HireMeFormTest(TestCase):

    def setUp(self):
        self.faker = Faker('en_US')

    def test_correct_input(self):
        form_data = {
                'name': 'John Smith',
                'email': 'jsmith@domain.com',
                'project_type': 'b',
                'project_status': 'e',
                'description': self.faker.text(max_nb_chars=1000)
        }
        form = HireMeForm(data=form_data)
        self.assertTrue(form.is_valid())


    def test_empty_name_field(self):
        form_data = {
                'name': '',
                'email': 'jsmith@domain.com',
                'project_type': 'b',
                'project_status': 'e',
                'description': self.faker.text(max_nb_chars=1000)
        }
        form = HireMeForm(data=form_data)
        self.assertEqual(form.errors['name'], [u'This field is required.'])

    def test_empty_email_field(self):
        form_data = {
                'name': 'John Smith',
                'email': '',
                'project_type': 'b',
                'project_status': 'e',
                'description': self.faker.text(max_nb_chars=1000)
        }
        form = HireMeForm(data=form_data)
        self.assertEqual(form.errors['email'], [u'This field is required.'])

    def test_empty_proj_description_field(self):
        form_data = {
                'name': 'John Smith',
                'email': 'jsmith@domain.com',
                'project_type': 'b',
                'project_status': 'e',
                'description': ''
        }
        form = HireMeForm(data=form_data)
        self.assertEqual(form.errors['description'], [u'This field is required.'])

    def test_none_proj_type(self):
        form_data = {
                'name': 'John Smith',
                'email': 'jsmith@domain.com',
                'project_type': '',
                'project_status': 'e',
                'description': self.faker.text(max_nb_chars=1000)
        }
        form = HireMeForm(data=form_data)
        self.assertEqual(form.errors['project_type'], [u'This field is required.'])

    def test_none_proj_status(self):
        form_data = {
                'name': 'John Smith',
                'email': 'jsmith@domain.com',
                'project_type': 'b',
                'project_status': '',
                'description': self.faker.text(max_nb_chars=1000)
        }
        form = HireMeForm(data=form_data)
        self.assertEqual(form.errors['project_status'], [u'This field is required.'])

    def test_wrong_email(self):
        wrong_emails = ['jsmithdoamin.com', 'jsmith@', '@domain.com']

        for wrong_email in wrong_emails:
            form_data = {
                    'name': 'John Smith',
                    'email': wrong_email,
                    'project_type': 'b',
                    'project_status': 'e',
                    'description': self.faker.text(max_nb_chars=1000)
            }
            form = HireMeForm(data=form_data)
            self.assertEqual(form.errors['email'], [u'Enter a valid email address.'])

    def test_too_long_name(self):
        # Generate a string that has at least 51 chars
        long_string = make_long_string(min_nb_chars=51)

        form_data = {
                'name': long_string,
                'email': 'jsmith@domain.com',
                'project_type': 'b',
                'project_status': 'e',
                'description': self.faker.text(max_nb_chars=1000)
        }
        form = HireMeForm(data=form_data)
        self.assertEqual(form.errors['name'], [u'Ensure this value has at most 50 characters (it has ' + str(len(long_string)) + ').'])

    def test_too_long_email(self):
        # Generate a string that has at least 255 chars
        long_string = make_long_string(min_nb_chars=255)

        # Make it email-like
        long_string = long_string + '@domain.com'

        form_data = {
                'name': 'John Smith',
                'email': long_string,
                'project_type': 'b',
                'project_status': 'e',
                'description': self.faker.text(max_nb_chars=1000)
        }
        form = HireMeForm(data=form_data)
        self.assertEqual(
            form.errors['email'],
            [
                u'Enter a valid email address.',
                u'Ensure this value has at most 254 characters (it has ' + str(len(long_string)) + ').'
            ]
        )

    def test_too_long_description(self):
        # Generate a string that has at least 1001 chars
        long_string = make_long_string(min_nb_chars=1001)

        form_data = {
                'name': 'John Smith',
                'email': 'jsmith@domain.com',
                'project_type': 'b',
                'project_status': 'e',
                'description': long_string
        }
        form = HireMeForm(data=form_data)
        self.assertEqual(form.errors['description'], [u'Ensure this value has at most 1000 characters (it has ' + str(len(long_string)) + ').'])


class ContactFormTest(TestCase):

    def setUp(self):
        self.faker = Faker('en_US')

    def test_correct_input(self):
        form_data = {
                'name': 'John Smith',
                'email': 'jsmith@domain.com',
                'message': self.faker.text(max_nb_chars=1000)
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_empty_name_field(self):
        form_data = {
                'name': '',
                'email': 'jsmith@domain.com',
                'message': self.faker.text(max_nb_chars=1000)
        }
        form = ContactForm(data=form_data)
        self.assertEqual(form.errors['name'], [u'This field is required.'])

    def test_empty_email_field(self):
        form_data = {
                'name': 'John Smith',
                'email': '',
                'message': self.faker.text(max_nb_chars=1000)
        }
        form = ContactForm(data=form_data)
        self.assertEqual(form.errors['email'], [u'This field is required.'])

    def test_empty_message_field(self):
        form_data = {
                'name': 'John Smith',
                'email': 'jsmith@domain.com',
                'message': ''
        }
        form = ContactForm(data=form_data)
        self.assertEqual(form.errors['message'], [u'This field is required.'])

    def test_wrong_email(self):
        wrong_emails = ['jsmithdoamin.com', 'jsmith@', '@domain.com']

        for wrong_email in wrong_emails:
            form_data = {
                    'name': 'John Smith',
                    'email': wrong_email,
                    'message': self.faker.text(max_nb_chars=1000)
            }
            form = ContactForm(data=form_data)
            self.assertEqual(form.errors['email'], [u'Enter a valid email address.'])

    def test_too_long_name(self):
        # Generate a string that has at least 51 chars
        long_string = make_long_string(min_nb_chars=51)

        form_data = {
                'name': long_string,
                'email': 'jsmith@domain.com',
                'message': self.faker.text(max_nb_chars=1000)
        }
        form = ContactForm(data=form_data)
        self.assertEqual(form.errors['name'], [u'Ensure this value has at most 50 characters (it has ' + str(len(long_string)) + ').'])

    def test_too_long_email(self):
        # Generate a string that has at least 255 chars
        long_string = make_long_string(min_nb_chars=255)

        # Make it email-like
        long_string = long_string + '@domain.com'

        form_data = {
                'name': 'John Smith',
                'email': long_string,
                'message': self.faker.text(max_nb_chars=1000)
        }
        form = ContactForm(data=form_data)
        self.assertEqual(
            form.errors['email'],
            [
                u'Enter a valid email address.',
                u'Ensure this value has at most 254 characters (it has ' + str(len(long_string)) + ').'
            ]
        )

    def test_too_long_description(self):
        # Generate a string that has at least 1001 chars
        long_string = make_long_string(min_nb_chars=1001)

        form_data = {
                'name': 'John Smith',
                'email': 'jsmith@domain.com',
                'message': long_string
        }
        form = ContactForm(data=form_data)
        self.assertEqual(form.errors['message'], [u'Ensure this value has at most 1000 characters (it has ' + str(len(long_string)) + ').'])

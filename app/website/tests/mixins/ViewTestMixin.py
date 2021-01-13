from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.test import RequestFactory
from django.urls import resolve
from django.urls.exceptions import Resolver404

# Based on the https://blog.bitlabstudio.com/proper-unit-tests-for-your-django-views-b4a1730a922e
class ViewTestMixin(object):
    """Mixin with shortcuts for view tests."""
    longMessage = True  # More verbose error messages
    view_class = None

    def get_view_kwargs(self):
        """
        Returns a dictionary representing the view's kwargs, if
        necessary.

        If the URL of this view is constructed via kwargs, you can
        override this method and return the proper kwargs for the
        test.

        """
        return {}

    def get_response(self, method, user, data, args, kwargs):
        """
        Creates a request and a response object.

        method  'get' or 'post' requests to be send (read more below)
        user    user sending request (if None, will be set to anonymous)
        data    dictionary of data substituted into the form

        args and kwargs are passed over to the view_class along with the request
        """
        # Create an instance of RequestFactory() class, i.e. create a request
        factory = RequestFactory()
        # Data passed as kwargs with the request (e.g. form input)
        req_kwargs = {}

        if data:
            req_kwargs.update({'data': data})

        # Below syntax is equivalent to req_factory.get('/') (assuming method =
        # get), although it allows for dynamically changing method
        req = getattr(factory, method)('/', **req_kwargs)
        # Set the user type if any provided, else set it as anonymous
        req.user = user if user else AnonymousUser()
        return self.view_class.as_view()(req, *args, **kwargs)

    def is_callable(
        self,
        user=None,
        post=False,
        to=None,
        data={},
        args=[],
        kwargs={},
    ):
        """
        Initiates a call and tests the outcome.

        user    user sending request
        post    flag, set to true when sending a POST request
        to      view the user shall be redirected to after submitting the form
        data    dictionary of data substituted into the form

        args and kwargs are passed over to the get_response() function to later
        be passed to the view_class along with the request
        """
        view_kwargs = kwargs or self.get_view_kwargs()
        resp = self.get_response(
            'post' if post else 'get',
            user=user,
            data=data,
            args=args,
            kwargs=view_kwargs,
        )

        # I.e. if there is a page to redirect to provided, else execute as if it
        # was a normal get request.
        # The below has three outcomes. First one is POST request with provided
        # accessible success page, the second one is POST request with 'to' page
        # that doesn't work (failure, Resolver404) and the third one is no
        # success page provided
        if to:
            self.assertIn(
                resp.status_code, [301, 302],
                msg='The request was not redirected.'
            )

            # Splits response.url into a list based on '?' and '#' chars, then
            # only the first element is taken after each transformation. E.g.
            # 'Hello#my name?is Jerry and#I#love?everyone.' would end up as:
            # ['Hello#my name', 'is Jerry and#I#love', 'everyone.'][0] ->
            # 'Hello#my name' -> ['Hello', 'my name'][0] -> 'Hello'. It cleans
            # up the response from potential unnecessary part.
            resp_url = resp.url.split('?')[0].split('#')[0]

            try:
                self.assertEqual(
                    resolve(resp_url).url_name,
                    to,
                    msg='Should redirect to "{}".'.format(to)
                )
            except Resolver404:
                raise Exception(
                    'Could not resolve "{}".'.format(resp.url)
                )
        else:
            self.assertEqual(resp.status_code, 200)

    def is_not_callable(self, **kwargs):
        """Tests if call raises a 404."""
        with self.assertRaises(Http404):
            self.is_callable(**kwargs)

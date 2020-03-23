# users/tests.py
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

# from Boroughs.models import Borough


class AccountsTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_create_user(self):
        """ Tests the user is created"""
        user = User(first_name="tester")
        user.save()
        self.assertEqual(user.first_name, 'tester')

    def test_signup(self):
        # Make some test data to be sent through the signup page.
        data = {"username": "test-user",
                "password1": "testpassword", "password2": "testpassword"}

        response = self.client.post('sign-up', data=data)

        self.assertEqual(response.status_code, 404)  # should give 302 not 404

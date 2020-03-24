# boroughs/tests.py
# from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.test import TestCase

from Boroughs.models import Borough, Photo


class BoroughTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        """ Tests the slug generated when saving a Page. """
        # Author is a required field in our model.
        # Create a user for this test and save it to the test database.
        user = settings.AUTH_USER_MODEL.objects.create()

        # Create and save a new page to the test database.
        page = Borough(title="My Test Page", content="test", author=user)
        page.save()

        # Make sure the slug that was generated in Page.save()
        # matches what we think it should be.
        self.assertEqual(page.slug, "my-test-page")


class BoroughListViewTests(TestCase):
    def test_multiple_pages(self):
        # Make some test data to be displayed on the page.
        user = settings.AUTH_USER_MODEL.objects.create()

        Borough.objects.create(title="My Test Page", content="test", author=user)
        Borough.objects.create(title="Another Test Page", content="test", author=user)

        # Issue a GET request to the 37 boroughs list page.
        # When we make a request, we get a response back.
        response = self.client.get('/Boroughs/models/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the number of pages passed to the template
        # matches the number of pages we have in the database.
        responses = response.context['Boroughs']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Borough: My Test Page>', '<Borough: Another Test Page>'],
            ordered=False
        )


class BoroughDetailViewTests(TestCase):
    def test_slug(self):
        # Make some test data to be displayed on the page.
        user = settings.AUTH_USER_MODEL.objects.create()

        page1 = Borough.objects.create(
            title="My Test Page", content="test", author=user)
        page2 = Borough.objects.create(
            title="Another Test Page", content="test", author=user)

        # Make sure the slug that was generated in Page.save()
        # matches what we think it should be.
        self.assertEqual(page1.slug, "my-test-page")
        self.assertEqual(page2.slug, "another-test-page")

        url1 = reverse('borough-details', args=[page1.slug])
        url2 = reverse('borough-details', args=[page2.slug])

        # Issue a GET request to the MakeWiki Detail page.
        # When we make a request, we get a response back.
        response1 = self.client.get(url1)
        response2 = self.client.get(url2)

        # Check that the response is 200 OK.
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)


class BoroughCreateViewTest(TestCase):
    def test(self):
        user = settings.AUTH_USER_MODEL.objects.create()

        # Make some test data to be sent through the create page.
        data = {
            "title": "my-test-page",
            "zipcode": "9410",
            "content": "test",
            "main_img": "{% static 'images/Landing/chinatown-nobhill-main.png' %}",
            "sources": "https://google.com",
            "author": user
        }

        response = self.client.post('/Boroughs/create-borough', data=data)

        self.assertEqual(response.status_code, 301)

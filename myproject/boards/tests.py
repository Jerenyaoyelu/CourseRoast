from django.test import TestCase
from django.urls import reverse,resolve
from .views import home

# Create your tests here.
#error 500: internal server error
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)

    #Django uses the resolve function to match a requested URL 
    #with a list of URLs listed in the urls.py module. 
    #This test will make sure the URL /, which is the root URL, is returning the home view
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func,home)

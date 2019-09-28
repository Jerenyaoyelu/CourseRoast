from django.test import TestCase
from django.urls import reverse,resolve
from .views import home, board_topics
from .models import Board

# Create your tests here.
#error 500: internal server error
class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django',description='Django board')
        #move url and response to setUp, so that we can reuse the same response
        url=reverse('home')
        self.response=self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code,200)

    #Django uses the resolve function to match a requested URL 
    #with a list of URLs listed in the urls.py module. 
    #This test will make sure the URL /, which is the root URL, is returning the home view
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func,home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics',kwargs={'pk':self.board.pk})
        #assertContains method tests if the response body contains a given text
        self.assertContains(self.response,'href="{0}"'.format(board_topics_url))

class BoardTopicSTests(TestCase):
    #this creates a Board instance to use in the tests
    #it is compulsory, because django testing suite doesnt run your tests against the current DB
    #to run the tests,django creates a new DB on the fly, applies all model migrations,
    #runs the tests,and when done,destroys the testing DB
    #so this method prepares the env to run tests, so to simulate a scenario
    def setUp(self):
        Board.objects.create(name='Django',description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics',kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics',kwargs={'pk':99})
        response = self.client.get(url)
        self.assertEquals(response.status_code,404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view=resolve('/boards/1/')
        self.assertEquals(view.func,board_topics)
    #link back test
    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url=reverse('board_topics',kwargs={'pk':1})
        response=self.client.get(board_topics_url)
        homepage_url=reverse('home')
        self.assertContains(response,'href="{0}"'.format(homepage_url))
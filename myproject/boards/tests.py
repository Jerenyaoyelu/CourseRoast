from django.test import TestCase
from django.urls import reverse,resolve
#every time adding a new page, needs to import
from .views import home, board_topics, new_topic
from .models import Board, Post, Topic
from django.contrib.auth.models import User
from .forms import NewTopicForm

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

    #test for making sure that the user can reach new topic view
    def test_board_topics_view_contains_navigation_links(self):
        board_topics_url=reverse('board_topics',kwargs={'pk':1})
        homepage_url=reverse('home')
        new_topic_url=reverse('new_topic',kwargs={'pk':1})

        response=self.client.get(board_topics_url)

        self.assertContains(response,f'href="{homepage_url}"')
        self.assertContains(response,f'href="{new_topic_url}"')

class NewTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django',description='Course roast!')

    def test_new_topic_view_success_status_code(self):
        url=reverse('new_topic',kwargs={'pk':1})
        response=self.client.get(url)
        self.assertEquals(response.status_code,200)

    def test_new_topic_view_not_found_status_code(self):
        url=reverse('new_topic',kwargs={'pk':99})
        response=self.client.get(url)
        self.assertEquals(response.status_code,404)

    def test_new_topic_url_resolves_new_topic_view(self):
        view=resolve('/boards/1/new/')
        #have to import new_topic
        self.assertEquals(view.func,new_topic)

    def test_new_topic_view_contains_link_back_to_board_topics_view(self):
        new_topic_url=reverse('new_topic',kwargs={'pk':1})
        board_topics_url=reverse('board_topics',kwargs={'pk':1})
        response=self.client.get(new_topic_url)
        self.assertContains(response,f'href="{board_topics_url}"')

    def test_csrf(self):#make sure our HTML contains the token
        url=reverse('new_topic',kwargs={'pk':1})
        response=self.client.get(url)
        self.assertContains(response,'csrfmiddlewaretoken')

    def test_new_topic_valid_post_data(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        # #when testing, NOT NULL constraint error occurs
        test_user = User.objects.create(password= "asasas123")
        data = {
            'subject': 'Test title',
            'message': 'Lorem ipsum dolor sit amet',
            'starter':test_user
        }
        response = self.client.post(url, data)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())

    def test_new_topic_invalid_post_data(self):
        '''
        invalid post data should not redirect
        the expected behavior is to show the form again with validation errors
        '''
        url=reverse('new_topic',kwargs={'pk':1})
        response=self.client.post(url,{})#sending empty dict to check how the app is behaving
        form=response.context.get('form')
        self.assertEquals(response.status_code,200)
        #make sure the form is showing errors when the data is invalid
        self.assertTrue(form.errors)

    def test_new_topic_invalid_post_data_empty_fields(self):
        '''
        invalid post data should not redirect
        the expected behavior is to show the form again with validation errors
        '''
        #sending some data, expectation is to validate and reject empty subject and message
        url=reverse('new_topic',kwargs={'pk':1})
        data={
            'suject':'',
            'message':''
        }
        response=self.client.post(url,data)
        self.assertEquals(response.status_code,200)
        self.assertFalse(Topic.objects.exists())
        self.assertFalse(Post.objects.exists())

    def test_contains_form(self):
        url=reverse('new_topic',kwargs={'pk':1})
        response=self.client.get(url)
        form=response.context.get('form')
        #grab form instance in the context data and check if it is a NewTopicForm
        self.assertIsInstance(form,NewTopicForm)

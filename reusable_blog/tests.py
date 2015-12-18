from django.test import TestCase
from .models import Post

# Create your tests here.

class PostTests(TestCase):
    def test_str(self):
        test_title = Post(post_title = 'My Latest Blog Post')

        #check if two variables are equal to each other
        self.assertEquals(
            str(test_title),'My Latest Blog Post'
        )
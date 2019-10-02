from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    description = models.CharField(max_length = 100)

    #__str__ method is a string representation of an object
    #we can use board name to represent it
    def __str__(self):
        return str(self.id) + ":" + self.name

class Topic(models.Model):
    subject = models.CharField(max_length = 255)
    last_update = models.DateTimeField(auto_now_add = True)
    board = models.ForeignKey(Board,on_delete = models.CASCADE,related_name = 'topics')
    #blank=True,null=True should solve the NOT NULL constraints error as well in the tests.py
    #but no, why??
    starter = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'topics')

class Post(models.Model):
    message = models.TextField(max_length = 400)
    created_at = models.DateTimeField(auto_now_add = True)

    topic = models.ForeignKey(Topic,on_delete = models.CASCADE,related_name = 'posts')
    updated_at = models.DateTimeField(null = True)
    created_by = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'posts')
    updated_by = models.ForeignKey(User,on_delete = models.CASCADE,null = True,related_name = '+')
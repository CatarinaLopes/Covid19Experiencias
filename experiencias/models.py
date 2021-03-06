import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class UserPost(models.Model):
    text = models.CharField(max_length=500)
    img = models.CharField(max_length=500)
    title = models.CharField(max_length=100)
    pub_data = models.DateTimeField('publishing date')
    user_name = models.CharField(max_length=25, default='')
    score = models.IntegerField(default=0)


class UserComment(models.Model):
    user_name = models.CharField(max_length=25, default='')
    text = models.CharField(max_length=500)
    pub_data = models.DateTimeField('publishing date')
    user_post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
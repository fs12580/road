# coding: utf-8
from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length = 100) #文章题目
    content = models.TextField(blank = True,null = True) #文章正文

    def __str__(self):
        return self.title
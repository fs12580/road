# coding: utf-8
from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class Article(models.Model):

    CATEGORY_CHOICES = [
        ('政策', '政策'),
        ('文化', '文化'),
        ('资讯', '资讯')
    ]
    headimg = models.CharField('头像', max_length=200, blank=True, null=True)
    title = models.CharField(max_length=100)  # 文章题目
    category = models.CharField(
        '类型', max_length=10, choices=CATEGORY_CHOICES, default='政策')
    introduction = models.TextField(blank=True, null=True)  # 文章摘要
    content = models.TextField(blank=True, null=True)  # 文章正文

    def __str__(self):
        return self.title


class Music(models.Model):
    name = models.CharField('歌名', max_length=100)
    musicurl = models.CharField('歌曲地址', max_length=200, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField('视频名', max_length=100)
    movieurl = models.CharField('视频地址', max_length=200, null=True)

    def __str__(self):
        return self.name


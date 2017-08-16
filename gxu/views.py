from django.shortcuts import render
# from django.http import HttpResponse
from .models import Article
from .models import Music
from .models import Video
from django.http import Http404

# 主页面


def index(request):
    list = ['政策', '资讯', '文化']
    data = {
        'policy': Article.objects.filter(category=list[0])[0:2],
        'information': Article.objects.filter(category=list[1]),
        'culture': Article.objects.filter(category=list[2])[0:4],
        'music': Music.objects.all()[0:3],
        'video': Video.objects.all()[0:3]
    }
    return render(request, 'gxu/index.html', data)


# 文章
def article_list(request, category):
    # post_list = Article.objects.all()[:2]
    list = ['政策', '资讯']
    if category == '1':
        data = {
            'index': 'policy',
            'article': Article.objects.filter(category=list[int(category) - 1])
        }
    if category == '2':
        data = {
            'index': 'information',
            'article': Article.objects.filter(category=list[int(category) - 1])
        }
    if category == '3':
        data = {
            'index': 'culture',
            'music': Music.objects.all(),
            'video': Video.objects.all()
        }
    if category == '4':
        data = {
            'index': 'we'
        }
    return render(request, 'gxu/article_list.html', data)


# 文章页
def article_detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'gxu/article_detail.html', {'post': post})


def music(request, id):
    try:
        data = {
            'post': Music.objects.get(id=str(id)),
            'index': 'culture',
            'culture': 'music'

        }
    except Music.DoesNotExist:
        raise Http404
    return render(request, 'gxu/article_detail.html', data)


def video(request, id):
    try:
        data = {
            'post': Video.objects.get(id=str(id)),
            'index': 'culture',
            'culture': 'video'

        }
    except Video.DoesNotExist:
        raise Http404
    return render(request, 'gxu/article_detail.html', data)


# 文化
def culture(request):
    return render(request, 'gxu/culture.html')


# 文化1.1
def culture1(request):
    return render(request, 'gxu/culture1.html')


# 资讯
def information(request):
    post_list = Article.objects.all()[2:6]
    return render(request, 'gxu/information.html', {'post_list': post_list})


# 资讯
def ours(request):
    return render(request, 'gxu/ours.html')

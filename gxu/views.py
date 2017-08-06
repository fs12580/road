from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.http import Http404

#主页面
def index(request):
    post_list = Article.objects.all()
    return render(request, 'gxu/index.html', {'post_list': post_list})


#文章页
def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'gxu/post.html', {'post': post})


#文化
def culture(request):
	return render(request, 'gxu/culture.html')


#文化1.1
def culture1(request):
	return render(request, 'gxu/culture1.html')


#政策
def policy(request):
	post_list = Article.objects.all()[:2]
	return render(request, 'gxu/policy.html', {'post_list': post_list})


#资讯
def information(request):
    post_list = Article.objects.all()[2:6]
    return render(request, 'gxu/information.html', {'post_list': post_list})
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.

def index(request):
    return render(request, 'gxu/index.html')


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'gxu/post.html', {'post': post})
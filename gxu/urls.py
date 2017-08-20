from django.conf.urls import url
from gxu import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),  # 主页
    url(r'^music/(\d+)$', views.music, name='music'),  # 音乐
    url(r'^video/(\d+)$', views.video, name='video'),  # 视频
    url(r'^article_list/(\d+)$', views.article_list,
        name='article_list'),  # 政策
    url(r'^article_detail/(\d+)$', views.article_detail,
        name='article_detail'),  # 政策文章页
    url(r'^search/$', views.search, name='search'),  # 搜索
]

from django.conf.urls import url
from gxu import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),  # 主页
    # url(r'^(?P<id>\d+)/$', views.detail, name='detail'),  # 咨询
    url(r'^culture/$', views.culture, name='culture'),  # 文化
    url(r'^culture1/$', views.culture1, name='culture1'),  # 文化1.1
    url(r'^article_list/(\d+)$', views.article_list,
        name='article_list'),  # 政策
    url(r'^article_detail/(\d+)$', views.article_detail,
        name='article_detail'),  # 政策文章页
    url(r'^information/$', views.information, name='information'),  # 资讯
    url(r'^ours/$', views.information, name='ours'),  # 资讯
]

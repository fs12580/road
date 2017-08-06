from django.conf.urls import include, url
from django.contrib import admin
from gxu import views as gxu_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'road.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', gxu_views.index, name='index'), #主页
    url(r'^(?P<id>\d+)/$', gxu_views.detail, name= 'detail'),#咨询
    url(r'^culture/$', gxu_views.culture, name= 'culture'),#文化
    url(r'^culture1/$', gxu_views.culture1, name= 'culture1'),#文化1.1
    url(r'^policy/$', gxu_views.policy, name='policy'),#政策
    url(r'^information/$', gxu_views.information, name='information'),#资讯
]

from django.conf.urls import include, url
from django.contrib import admin
from gxu import views as gxu_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'road.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', gxu_views.index, name='index'), 
    url(r'^(?P<id>\d+)/$', gxu_views.detail, name= 'detail'),
]

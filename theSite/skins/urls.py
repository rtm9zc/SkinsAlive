from django.conf.urls import patterns, include, url
from django.contrib import admin
from skins import views

urlpatterns = patterns('',
    url(r'^', views.index, name='index'),
    # Examples:
    # url(r'^$', 'skins.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import include, url
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from blog.models import Blog
from .views import BlogView, BlogList, add_subscriber


urlpatterns = [
    url(r'^$', BlogList.as_view(), name='blog_list'),
    url(r'^(?P<slug>[^/]+)/$', BlogView.as_view()
        , name='blog_detail'),
    url(r'^add_subscriber/$', add_subscriber, name='add_subscriber'),
    ]

from django.conf.urls import include, url
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from blog.models import Blog
from .views import add_contact_form, add_subscriber


urlpatterns = [
    url(r'^contact_form/$', add_contact_form, name='add_contact_form'),
    url(r'^add_subscriber/$', add_subscriber, name='add_subscriber'),
 ]

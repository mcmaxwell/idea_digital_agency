from django.conf.urls import include, url
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from cases.models import Case
from .views import CaseView


urlpatterns = [
    #url(r'^$', BlogList.as_view(), name='blog_list'),
    url(r'^(?P<slug>[^/]+)/$', CaseView.as_view()
        , name='case_detail')
    ]

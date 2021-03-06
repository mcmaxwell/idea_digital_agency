"""Idea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.utils.functional import curry
from django.views.defaults import server_error, page_not_found, permission_denied
from feincms.module.page.models import Page
from info.views import site_map

handler404 = curry(page_not_found, template_name='404.html')

urlpatterns = [
    url(r'^agency_start/', admin.site.urls),
    url(r'^sitemap\.xml$', site_map),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'', include('feincms.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

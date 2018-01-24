# from django.db import models
from feincms.module.page.models import Page
from django.utils.translation import ugettext_lazy as _
from .content_types import IndexPageInfoCT
from feincms.content.application.models import ApplicationContent

# Create your models here.

Page.register_extensions(
    'feincms.extensions.changedate',
    'feincms.extensions.translations',
    'feincms.module.page.extensions.navigation',
    'feincms.module.page.extensions.navigationgroups',
    'feincms.extensions.seo',
    'feincms.module.page.extensions.titles'
)  # Example set of extensions


Page.register_templates({
    'title': _('Page'),
    'path': 'content/pages/page.html',
    'regions': (
        ('main', _('Main content area')),
    ),
})


Page.register_templates({
    'title': _('Index Page'),
    'path': 'content/pages/index_page.html',
    'regions': (
        ('main', _('Main content area')),
    ),
})

Page.create_content_type(IndexPageInfoCT)

Page.create_content_type(ApplicationContent, APPLICATIONS=(
    ('blog.urls', 'Blog application'),
    ('cases.urls', 'Cases category'),
    ('info.urls', 'Info app'),
))

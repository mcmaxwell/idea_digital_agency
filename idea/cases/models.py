from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from redactor.fields import RedactorField
from django.utils import translation
from feincms.apps import app_reverse
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
from unidecode import unidecode
from sorl.thumbnail import get_thumbnail


@python_2_unicode_compatible
class Case(models.Model):

    image_preview = models.ImageField()

    image_top = models.ImageField()

    activity_title = models.CharField(
        max_length=255,
        verbose_name=_('activity_title'),
        null=True,
    )

    title = models.CharField(
        max_length=255,
        verbose_name=_('title'),
        null=True,
    )

    client = models.CharField(
        max_length=255,
        verbose_name=_('client'),
        null=True,
    )

    project = models.CharField(
        verbose_name= _('project'),
        max_length=255,
        blank=True,
        null=True
    )

    case_site = models.CharField(
        verbose_name= _('case_site'),
        max_length=255,
        blank=True,
        null=True
    )

    text = models.TextField(
        verbose_name= _('text'),
        blank=True,
        null=True
    )

    pictures_editor = models.TextField(
        verbose_name= _('pictures_editor'),
        blank=True,
        null=True
    )


    seo_title = models.CharField(blank=True, max_length=255)

    seo_keywords = models.CharField(blank=True, max_length=255)

    seo_description = models.CharField(blank=True, max_length=255)


    facebook_link = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('facebook_link'))
    insta_link = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('insta_link'))
    twitter_link = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('twitter_link'))
    behance_link = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('behance_link'))


    def get_image_top(self):
        return get_thumbnail(self.image_top,'1350x500', crop="center", quality=99).url


    def get_image_preview(self):
        return get_thumbnail(self.image_preview,'300x300',  quality=99).url

    def get_absolute_url(self):
      return app_reverse('case_detail', 'cases.urls', kwargs={
           'slug': self.slug,
        })

    slug = models.SlugField(blank=True, null=True)

    def save(self):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(Case, self).save()

    def get_case_services(self):
           return self._service_case.all()


    def __str__(self):
       return self.title

    class Meta:
      verbose_name = _('Case')
      verbose_name_plural = _('Case')
      ordering = ('-id',)


@python_2_unicode_compatible
class CaseService(models.Model):

    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    case = models.ForeignKey(Case, related_name='_service_case')

    title = models.CharField(
                max_length=255,
                verbose_name=_('title'),
                null=True,
    )


    def __str__(self):
        return self.case.title

    class Meta:
        ordering = ('order',)
        verbose_name = _('CaseService')
        verbose_name_plural = _('CaseService')

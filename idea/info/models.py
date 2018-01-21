from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from cloudinary.models import CloudinaryField
from redactor.fields import RedactorField
from django.utils.translation import ugettext_lazy as _
from feincms.apps import app_reverse
from common.utils import get_cloudinary_thumb
from django.utils.dateformat import DateFormat
from django.core.validators import RegexValidator, URLValidator
from sorl.thumbnail import get_thumbnail


@python_2_unicode_compatible
class Info(models.Model):

    adress_footer = models.CharField(blank=False, null=False, max_length=255, verbose_name=_('adress'))
    email_footer = models.CharField(blank=False, null=False, max_length=255, verbose_name=_('email'))
    phone_footer = models.CharField(blank=False, null=False, max_length=255, verbose_name=_('phone_footer'))
    facebook_link = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('facebook_link'))
    insta_link = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('insta_link'))
    twitter_link = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('twitter_link'))
    behance_link = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('behance_link'))

    def __str__(self):
        return self.adress_footer

    class Meta:
        verbose_name = _('Info')
        verbose_name_plural = _('Info')
        ordering = ['adress_footer',]

@python_2_unicode_compatible
class Subscriber(models.Model):

    name = models.CharField(blank=False, null=False, max_length=255, verbose_name=_('name'))
    email = models.CharField(blank=False, null=False, max_length=255, verbose_name=_('email'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Subscriber')
        verbose_name_plural = _('Subscriber')
        ordering = ['name',]


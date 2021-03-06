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

    seo_title_blog = models.CharField(blank=True, max_length=255)

    seo_keywords_blog = models.CharField(blank=True, max_length=255)

    seo_description_blog = models.CharField(blank=True, max_length=255)


    def __str__(self):
        return "Site Information"

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

@python_2_unicode_compatible
class TeamMember(models.Model):

    image = models.ImageField()
    name = models.CharField(blank=False, null=False, max_length=255, verbose_name=_('name'))
    position = models.CharField(blank=False, null=False, max_length=255, verbose_name=_('position'))


    def get_image(self):
        return get_thumbnail(self.image,'248x248', quality=99).url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('TeamMember')
        verbose_name_plural = _('TeamMember')
        ordering = ['name',]

@python_2_unicode_compatible
class ContactInfo(models.Model):

    first_name = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('first_name'))
    second_name = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('second_name'))
    email = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('email'))
    phone = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('phone'))
    budget = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('budget'))
    company = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('company'))

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    message = RedactorField(
        verbose_name=_('message'),
        allow_file_upload=False,
        allow_image_upload=False,
        blank=True
    )

    def __str__(self):
        return self.first_name + "" + self.second_name

    class Meta:
        verbose_name = _('ContactInfo')
        verbose_name_plural = _('ContactInfo')
        ordering = ['first_name',]

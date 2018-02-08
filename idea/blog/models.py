from __future__ import unicode_literals, division
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from redactor.fields import RedactorField
from django.utils import translation
from feincms.apps import app_reverse
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
from unidecode import unidecode
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail


@python_2_unicode_compatible
class BlogTag(models.Model):

    tag = models.CharField(blank=False, null=False, max_length=255, verbose_name=_('tag'))

    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    seo_title = models.CharField(blank=True, max_length=255)

    seo_keywords = models.CharField(blank=True, max_length=255)

    seo_description = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('order',)



@python_2_unicode_compatible
class Blog(models.Model):

    image_preview = models.ImageField()

    image_top = models.ImageField()

    title = models.CharField(
        max_length=255,
        verbose_name=_('title'),
        null=True,
    )

    author = models.CharField(
        max_length=255,
        verbose_name=_('author'),
        null=True,
    )

    text = models.TextField(
        verbose_name= _('text'),
        blank=True,
        null=True
    )

    seo_title = models.CharField(blank=True, max_length=255)

    seo_keywords = models.CharField(blank=True, max_length=255)

    seo_description = models.CharField(blank=True, max_length=255)

    tags = models.ManyToManyField(BlogTag)

    subtitle_tag = models.ForeignKey(BlogTag, related_name="_subtitle_tag",blank=False, null=False)

    date = models.DateField(_('date'), null=True)

    rating = models.PositiveIntegerField(default=0, blank=True, null=True)

    votes = models.PositiveIntegerField(default=0, blank=True, null=True)


    def get_image_top(self):
        return get_thumbnail(self.image_top,'1280x720', upscale=True, crop='center',  quality=99).url

    def get_image_preview(self):
        return get_thumbnail(self.image_preview,'330x240', upscale=True, crop='center',  quality=99).url

    def get_subtitle_tag(self):
        return self.subtitle_tag.tag

    def get_rating(self):
        print self.rating
        print self.votes
        return round(self.rating / self.votes, 2)

    def get_rating_for_width(self):
        enter_number = round(self.rating / self.votes, 2)
        number_dec = str(enter_number).split(".")[1]
        if len(number_dec) < 2:
            return int(number_dec + str(0))
        else:
            return int(number_dec)
        #enter_number = str(enter_number.split(',')
        #return int(number_dec)

    def get_absolute_url(self):
      return app_reverse('blog_detail', 'blog.urls', kwargs={
           'slug': self.slug,
        })

    slug = models.SlugField(blank=True, null=True)

    def save(self):
        if not self.slug:
            self.slug = str(self.id) + "-" + slugify(unidecode(self.title))
        super(Blog, self).save()


    def __str__(self):
       return self.title

    class Meta:
      verbose_name = _('Blog')
      verbose_name_plural = _('Blog')
      ordering = ('-id',)

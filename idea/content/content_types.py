from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from common.content_types import RenderCTMixin
from common.utils import get_cloudinary_thumb
from redactor.fields import RedactorField
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext
from django.template.loader import render_to_string
from sorl.thumbnail import get_thumbnail
from cases.models import Case
from info.models import Info
# @python_2_unicode_compatible
# class ParagraphCT(RenderCTMixin, models.Model):
#     template_name = "content/content_types/text_ct.html"
#     title = models.CharField(blank=False, max_length=255, verbose_name=_('title'))
#     text = RedactorField(
#         verbose_name=_('text'),
#         allow_file_upload=False,
#         allow_image_upload=False,
#         blank=True
#     )

#     def __str__(self):
#         return self.title

#     class Meta:
#         abstract = True
#         verbose_name = _('paragraph')
#         verbose_name_plural = _('paragraphes')

class IndexPageInfoCT(RenderCTMixin, models.Model):
    template_name = "content/content_types/index_page_content.html"

    title = RedactorField(
        verbose_name=_('title'),
        allow_file_upload=False,
        allow_image_upload=False,
        blank=False
    )

    sub_title = models.CharField(blank=False, max_length=255, verbose_name=_('sub_title'))

    text_about_us = RedactorField(
        verbose_name=_('text_about_us'),
        allow_file_upload=False,
        allow_image_upload=False,
        blank=True
    )

    service_title_one = models.CharField(blank=False, max_length=255, verbose_name=_('service_title_one'))

    service_list_one = RedactorField(
        verbose_name=_('service_list_one'),
        allow_file_upload=False,
        allow_image_upload=False,
        blank=True
    )

    service_title_two = models.CharField(blank=False, max_length=255, verbose_name=_('service_title_two'))

    service_list_two = RedactorField(
        verbose_name=_('service_list_two'),
        allow_file_upload=False,
        allow_image_upload=False,
        blank=True
    )

    service_title_three = models.CharField(blank=False, max_length=255, verbose_name=_('service_title_three'))

    service_list_three = RedactorField(
        verbose_name=_('service_list_three'),
        allow_file_upload=False,
        allow_image_upload=False,
        blank=True
    )

    service_title_four = models.CharField(blank=False, max_length=255, verbose_name=_('service_title_four'))

    service_list_four = RedactorField(
        verbose_name=_('service_list_four'),
        allow_file_upload=False,
        allow_image_upload=False,
        blank=True
    )


    def get_template_data(self):
        cases = Case.objects.all()
        info = Info.objects.all()

        return {
            'ctx': self,
            'cases': cases,
            'info':info,
        }

    class Meta:
        abstract = True
        verbose_name = _('IndexPageInfoCT')
        verbose_name_plural = _('IndexPageInfoCT')

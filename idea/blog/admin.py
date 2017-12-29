# Register your models here.
from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from modeltranslation.admin import TabbedTranslationAdmin
from django.utils.html import format_html
from redactor.fields import RedactorField
from common.admin import CommonPostAdmin
from django import forms
from .models import Blog, BlogTag
from .translation import TranslationOptions
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
          'text': SummernoteWidget(),
        }


class BlogTagAdmin(TabbedTranslationAdmin):
    list_display = ('tag',)
    fieldsets = (
        (_('Tag'), {
           'fields': ('tag', ),
       }),
    )
    sortable = 'order'
    


class BlogAdmin(CommonPostAdmin, TabbedTranslationAdmin):
    list_display = ('title_en',)
    formfield_overrides = {
        models.TextField : {'widget': SummernoteWidget},
    }

    sortable = 'order'
    filter_horizontal = ('tags',)
    fieldsets = (
        (_('Blog'), {
           'fields': ('image_preview', 'image_top','title', 'subtitle_tag','author','text', 'tags','date', ),
       }),
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogTag, BlogTagAdmin)

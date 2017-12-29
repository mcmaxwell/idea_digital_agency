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
from .models import Case, CaseService
from .translation import TranslationOptions
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class CaseAdminForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = '__all__'
        widgets = {
          'text': SummernoteWidget(),
        }

class CaseServiceInline(SortableInlineAdminMixin, admin.StackedInline):
    model = CaseService
    extra = 0
    fieldsets = (
        (_('CaseService'), {
            'fields': ('title',),
        }),
    )



class CaseAdmin(SortableAdminMixin, TabbedTranslationAdmin):
    list_display = ('title_en',)
    formfield_overrides = {
        models.TextField : {'widget': SummernoteWidget},
    }

    sortable = 'order'
    inlines = [
        CaseServiceInline,
    ]



admin.site.register(Case, CaseAdmin)


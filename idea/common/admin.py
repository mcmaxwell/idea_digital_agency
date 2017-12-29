from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html
from modeltranslation.admin import TabbedTranslationAdmin
from adminsortable2.admin import SortableAdminMixin


def admin_thumbnail_img(obj):
    return format_html('<img src=%s >' % obj.get_admin_thumbnail())


class CommonPostAdmin(SortableAdminMixin, TabbedTranslationAdmin):
    list_display = ('title_ru', 'created_at')
    date_hierarchy = 'date'
    sortable = 'order'


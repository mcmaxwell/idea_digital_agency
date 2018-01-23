from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.utils.html import format_html
from modeltranslation.admin import TabbedTranslationAdmin
from .translation import InfoTranslationOptions
from .models import Info, Subscriber, ContactInfo

def get_admin_thumbnail(self):
    return get_cloudinary_thumb(self.image, width=100, crop="fill", q=7)

def admin_thumbnail_img(obj):
    return format_html('<img src=%s >' % obj.get_admin_thumbnail())

# Register your models here.
class InfoAdmin(TabbedTranslationAdmin):
    def has_add_permission(self, request, obj=None):
        info = Info.objects.all()
        if len(info) == 1:
            return False
        else:
            return True

class SubscriberAdmin(admin.ModelAdmin):
	pass

admin.site.register(Info, InfoAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(ContactInfo, SubscriberAdmin)

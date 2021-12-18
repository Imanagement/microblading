from cms.admin.placeholderadmin import FrontendEditableAdminMixin
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from core.models import FAQ
from services.models import Service, GalleryImage, GalleryVideo, ExtraPrice
from testimonials.models import Testimonial


class GalleryImageAdminInline(admin.TabularInline):
    model = GalleryImage
    fields = ('image',)
    extra = 1


class GalleryVideoAdminInline(admin.TabularInline):
    model = GalleryVideo
    fields = ('url',)
    extra = 1


class FAQAdminInline(admin.TabularInline):
    model = FAQ
    fields = ('question', 'answer',)
    extra = 2


class ExtraPriceAdminInline(admin.TabularInline):
    model = ExtraPrice
    fields = ('name', 'cost')
    extra = 1


class ServiceAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
    inlines = (GalleryImageAdminInline, GalleryVideoAdminInline, FAQAdminInline, ExtraPriceAdminInline)
    frontend_editable_fields = ('name', 'teaser_description', 'description', 'cost', 'cost_name')


admin.site.register(Service, ServiceAdmin)

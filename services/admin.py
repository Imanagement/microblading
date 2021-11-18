from django.contrib import admin

from core.models import FAQ
from services.models import Service, GalleryImage, GalleryVideo
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


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    inlines = [GalleryImageAdminInline, GalleryVideoAdminInline, FAQAdminInline]


admin.site.register(Service, ServiceAdmin)

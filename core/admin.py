from django.contrib import admin
from .models import FAQ, ContactUsModel, Page


class PageAdminModel(admin.ModelAdmin):
    fields = ('page_name', 'page_slug', 'title', 'meta_description')


admin.site.register(ContactUsModel)
admin.site.register(FAQ)
admin.site.register(Page, PageAdminModel)


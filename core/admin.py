from django.contrib import admin
from .models import FAQ, ContactUsModel

admin.site.register(ContactUsModel)
admin.site.register(FAQ)

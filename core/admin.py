from django.contrib import admin
from .models import FAQ, ContactUsModel, HomeHeaderAddressModel, AsideNavigationFlag


admin.site.register(HomeHeaderAddressModel)
admin.site.register(AsideNavigationFlag)
admin.site.register(ContactUsModel)
admin.site.register(FAQ)


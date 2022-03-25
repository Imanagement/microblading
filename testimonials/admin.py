from django.contrib import admin
from .models import Testimonial


class TestimonialAdminModel(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": ('image_type',),
        }),
        ("Main options", {
            "fields": ('name', 'position', 'image', 'testimonial',)
        })
    )


admin.site.register(Testimonial, TestimonialAdminModel)

from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField

from services.models import Service


class Testimonial(models.Model):
    image_type = models.BooleanField(
        verbose_name=_('Testimonial - Image Type?'),
        default=True
    )
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=55,
        null=True,
        blank=True
    )
    position = models.CharField(
        verbose_name=_('Position'),
        max_length=55,
        null=True,
        blank=True
    )
    image = FilerImageField(
        verbose_name=_('Image'),
        on_delete=models.SET_NULL,
        null=True
    )
    testimonial = models.TextField(
        verbose_name=_('Testimonial'),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Testimonial')
        verbose_name_plural =_('Testimonials')

    def __str__(self):
        return _(f"Testimonial from {self.name if self.name else str(self.id) + ' client id'}")

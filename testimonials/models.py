from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField

from services.models import Service


class Testimonial(models.Model):
    image_type = models.BooleanField(
        verbose_name=_('Отзыв - фотография?'),
        default=True
    )
    name = models.CharField(
        verbose_name=_('Имя'),
        max_length=55,
        null=True,
        blank=True
    )
    position = models.CharField(
        verbose_name=_('Должность'),
        max_length=55,
        null=True,
        blank=True
    )
    image = FilerImageField(
        verbose_name=_('Изображение'),
        on_delete=models.SET_NULL,
        null=True
    )
    testimonial = models.TextField(
        verbose_name=_('Отзыв'),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural =_('Отзывы')

    def __str__(self):
        return f"Отзыв от {self.name if self.name else str(self.id) + ' id клиента'}"

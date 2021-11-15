from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


class Testimonial(models.Model):
    name = models.CharField(
        verbose_name=_('Имя'),
        max_length=55
    )
    position = models.CharField(
        verbose_name=_('Должность'),
        max_length=55
    )
    image = FilerImageField(
        verbose_name=_('Изображение'),
        on_delete=models.SET_NULL,
        null=True
    )
    testimonial = models.TextField(
        verbose_name=_('Отзыв')
    )

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural =_('Отзывы')

    def __str__(self):
        return f"Отзыв от {self.name}"

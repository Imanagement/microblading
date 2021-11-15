from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


class PortfolioItem(models.Model):
    name = models.CharField(
        verbose_name=_('Название'),
        max_length=55
    )
    image = FilerImageField(
        verbose_name=_('Изображение'),
        on_delete=models.SET_NULL,
        null=True,
    )
    alt_text = models.CharField(
        verbose_name=_('Альт изображения'),
        max_length=255,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Проект из Портфолио')
        verbose_name_plural = _('Портфолио')

    def __str__(self):
        return self.name
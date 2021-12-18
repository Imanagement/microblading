from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


class PortfolioItem(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=55
    )
    image = FilerImageField(
        verbose_name=_('Image'),
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name = _('Portfolio Project')
        verbose_name_plural = _('Portfolio Projects')

    def __str__(self):
        return self.name


class PortfolioRowPluginModel(CMSPlugin):
    fetch_from_db = models.BooleanField(
        verbose_name=_('Fetch from db?'),
        default=True
    )
    stretch = models.BooleanField(
        verbose_name=_('Stretch'),
        help_text=_('Full width of screen content'),
        default=False
    )

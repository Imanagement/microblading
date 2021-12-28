from djangocms_text_ckeditor.fields import HTMLField
from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from django.db import models
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField

from services.models import Service


class AsideNavigationFlag(models.Model):
    language = models.CharField(
        verbose_name=_('Language'),
        max_length=25,
        choices=settings.LANGUAGES
    )
    image = FilerImageField(
        verbose_name=_('Image'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.language


class FAQ(models.Model):
    service = models.ForeignKey(
        to=Service,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    question = models.CharField(
        verbose_name=_('Question'),
        max_length=255
    )
    answer = HTMLField(
        verbose_name=_('Answer'),
    )

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQ\'s')

    def __str__(self):
        return self.question


class ContactUsModel(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=55,
    )
    email = models.EmailField(
        verbose_name=_('Email'),
        null=True,
        blank=True
    )
    phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=35,
    )
    message = models.TextField(
        verbose_name=_('Message'),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Contact Us Offer')
        verbose_name_plural = _('Contact Us Offers')

    def __str__(self):
        return gettext(f"Contact Us Offer From {self.name}")


class HeaderSectionPluginModel(CMSPlugin):

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=155,
        null=True,
        blank=True
    )
    bg_image = FilerImageField(
        verbose_name=_('Background image'),
        on_delete=models.SET_NULL,
        null=True
    )


class TitlePluginModel(CMSPlugin):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=155,
    )
    subtitle = models.CharField(
        verbose_name=_('Subtitle'),
        max_length=155,
        null=True,
        blank=True
    )
    with_bg_image = models.BooleanField(
        verbose_name=_('With bg image?'),
        default=False
    )
    image = FilerImageField(
        verbose_name=_('Image in row'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    text_align = models.CharField(
        verbose_name=_('Text align'),
        default="L",
        choices=(('L', 'Left'), ('C', 'Center')),
        max_length=1
    )


class CounterItemPluginModel(CMSPlugin):
    icon = FilerImageField(
        verbose_name=_('Icon'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    prefix = models.CharField(
        verbose_name=_('Prefix'),
        max_length=5,
        null=True,
        blank=True
    )
    suffix = models.CharField(
        verbose_name=_('Suffix'),
        max_length=5,
        null=True,
        blank=True
    )
    value = models.PositiveSmallIntegerField(
        verbose_name=_('Value')
    )
    name = models.CharField(
        max_length=255,
    )


class AboutUsBlockPluginModel(CMSPlugin):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=155,
        null=True,
        blank=True
    )
    subtitle = models.CharField(
        verbose_name=_('Subtitle'),
        max_length=155,
        null=True,
        blank=True
    )
    image = FilerImageField(
        verbose_name=_('Image'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    content = HTMLField(
        verbose_name=_('Content'),
        null=True,
        blank=True
    )


class SectionPluginModel(CMSPlugin):
    full_width = models.BooleanField(
        verbose_name=_("Full Width"),
        help_text=_("Stretch section to full width of browser?"),
        default=False
    )
    background_image = FilerImageField(
        verbose_name=_('Background Image'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    background_gray = models.BooleanField(
        verbose_name=_('Background Gray'),
        help_text=_('This works only when background image is not set'),
        default=False
    )

class RowPluginModel(CMSPlugin):
    text_align = models.CharField(
        verbose_name=_('Text align'),
        null=True,
        blank=True,
        choices=(('left', 'Left'), ('center', 'Center'), ('right', 'Right')),
        max_length=15
    )
    horizontal_padding = models.CharField(
        max_length=25,
        verbose_name=_('Horizontal padding'),
        null=True,
        blank=True
    )
    vertical_padding = models.CharField(
        max_length=25,
        verbose_name=_('Vertical padding'),
        null=True,
        blank=True
    )


class ColumnPluginModel(CMSPlugin):
    xs = models.PositiveSmallIntegerField(
        verbose_name="X-Small",
        help_text="<767px",
        null=True,
        blank=True
    )
    sm = models.PositiveSmallIntegerField(
        verbose_name="Small",
        help_text="≥768px",
        null=True,
        blank=True
    )
    md = models.PositiveSmallIntegerField(
        verbose_name="Medium",
        help_text="≥992px",
        null=True,
        blank=True
    )
    lg = models.PositiveSmallIntegerField(
        verbose_name="Large",
        help_text="≥1200px",
        null=True,
        blank=True
    )
    offset_xs = models.PositiveSmallIntegerField(
        verbose_name=_('Offset x-small'),
        null=True,
        blank=True
    )
    offset_sm = models.PositiveSmallIntegerField(
        verbose_name=_('Offset small'),
        null=True,
        blank=True
    )
    offset_md = models.PositiveSmallIntegerField(
        verbose_name=_('Offset medium'),
        null=True,
        blank=True
    )
    offset_lg = models.PositiveSmallIntegerField(
        verbose_name=_('Offset large'),
        null=True,
        blank=True
    )
    hide_xs = models.BooleanField(
        verbose_name=_('Hide on x-small devices'),
        default=False
    )
    hide_sm = models.BooleanField(
        verbose_name=_('Hide on small devices'),
        default=False
    )
    hide_md = models.BooleanField(
        verbose_name=_('Hide on medium devices'),
        default=False
    )
    hide_lg = models.BooleanField(
        verbose_name=_('Hide on large devices'),
        default=False
    )
    gray_bg_color = models.BooleanField(
        verbose_name=_('Background Color - Gray'),
        default=False
    )


class SpacePluginModel(CMSPlugin):
    space_height = models.PositiveSmallIntegerField(
        verbose_name=_('Space height')
    )
    xs = models.PositiveSmallIntegerField(
        verbose_name="Space height on x-small devices",
        help_text="<767px",
        null=True,
        blank=True
    )
    sm = models.PositiveSmallIntegerField(
        verbose_name="Space height on small devices",
        help_text="≥768px",
        null=True,
        blank=True
    )
    md = models.PositiveSmallIntegerField(
        verbose_name="Space height on medium devices",
        help_text="≥992px",
        null=True,
        blank=True
    )
    lg = models.PositiveSmallIntegerField(
        verbose_name="Space height on large devices",
        help_text="≥1200px",
        null=True,
        blank=True
    )


class ImagePluginModel(CMSPlugin):
    image = FilerImageField(
        verbose_name=_('Image'),
        on_delete=models.SET_NULL,
        null=True
    )
    width = models.PositiveSmallIntegerField(
        verbose_name=_('Width'),
        null=True,
        blank=True
    )
    height = models.PositiveSmallIntegerField(
        verbose_name=_('Height'),
        null=True,
        blank=True
    )
    object_fit_cover = models.BooleanField(
        verbose_name=_('Cover image'),
        help_text=_('Useful when image stretched and you want to fix by cutting the edge'),
        default=False
    )


class GoogleMapPluginModel(CMSPlugin):
    src = models.CharField(
        verbose_name=_("Src"),
        help_text=_("Just copy src from iframe and paste here"),
        max_length=500
    )
    width = models.PositiveSmallIntegerField(
        verbose_name=_('Width'),
        null=True,
        blank=True
    )
    height = models.PositiveSmallIntegerField(
        verbose_name=_('Height'),
        null=True,
        blank=True
    )


class HomeHeaderPluginModel(CMSPlugin):
    logo = FilerImageField(
        verbose_name=_('Logo'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='logo'
    )
    background_image = FilerImageField(
        verbose_name=_('Background image'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='background_image'
    )

    # def copy_relations(self, oldinstance):
    #     # Before copying related objects from the old instance, the ones
    #     # on the current one need to be deleted. Otherwise, duplicates may
    #     # appear on the public version of the page
    #     self.address.all().delete()
    #
    #     for address in oldinstance.address.all():
    #         # instance.pk = None; instance.pk.save() is the slightly odd but
    #         # standard Django way of copying a saved model instance
    #         address.pk = None
    #         address.plugin = self
    #         address.save()


class HomeHeaderAddressModel(models.Model):
    # header = models.ForeignKey(
    #     to=HomeHeaderPluginModel,
    #     on_delete=models.SET_NULL,
    #     related_name='address',
    #     null=True,
    #     blank=True
    # )
    # simple_header = models.ForeignKey(
    #     to=HeaderSectionPluginModel,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )
    text = HTMLField(
        verbose_name=_('Text'),
    )

    def __str__(self):
        return f"Address - {self.text}"


class AnimatedPluginModel(CMSPlugin):
    animated = models.BooleanField(
        verbose_name=_('Animated'),
        default=True,
    )

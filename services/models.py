from djangocms_text_ckeditor.fields import HTMLField
from cms.models.fields import PlaceholderField
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


class Service(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=555
    )
    custom_slug = models.BooleanField(
        verbose_name=_('Custom Slug'),
        default=False
    )
    slug = models.SlugField(
        verbose_name=_('Slug'),
        unique=True,
        blank=True,
        null=True,
        max_length=555
    )
    header = PlaceholderField(
        'header',
        related_name='header'
    )
    content = PlaceholderField(
        'content',
        related_name='content'
    )
    extra_content = PlaceholderField(
        'extra',
        related_name='extra'
    )

    # header_image = FilerImageField(
    #     verbose_name=_('Header Image'),
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='header_image'
    # )
    cost = models.PositiveIntegerField(
        verbose_name=_('Cost'),
    )
    cost_name = models.CharField(
        verbose_name=_('Cost Name'),
        max_length=155,
        null=True,
        blank=True
    )
    duration = models.PositiveIntegerField(
        verbose_name=_('Duration'),
        default=60
    )
    teaser_description = models.CharField(
        max_length=575,
        verbose_name=_('Intro Text'),
        help_text=_('Text which is seen from other pages (Teaser)'),
        null=True,
        blank=True
    )
    description = HTMLField(
        verbose_name=_('Description'),
        null=True,
        blank=True
    )
    description_image = FilerImageField(
        verbose_name=_('Description Image'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='description_image'
    )
    video_url = models.CharField(
        max_length=575,
        verbose_name=_('Video Url'),
        null=True,
        blank=True
    )
    icon = FilerImageField(
        verbose_name=_('Icon'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='icon'
    )

    # Seo
    h1_title = models.CharField(
        verbose_name=_('H1 Title'),
        max_length=255,
        null=True,
        blank=True
    )
    page_title = models.CharField(
        verbose_name=_('Seo Page Title'),
        max_length=255,
        null=True,
        blank=True
    )
    meta_description = models.TextField(
        verbose_name=_('Meta Description'),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def get_absolute_url(self):
        return reverse('services:service-detail', kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        # if self.video_url:
        #     url = self.video_url
        #     word_to_change = url.replace('watch?v=', 'embed/')
        #     self.video_url = word_to_change
        current_language = translation.get_language()
        if not self.custom_slug:
            translation.activate('en')
            if self.name:
                self.slug = slugify(self.name)
            translation.activate('es')
            if self.name:
                self.slug = slugify(self.name)
            translation.activate(current_language)
        super().save(*args, **kwargs)


class ExtraPrice(models.Model):
    service = models.ForeignKey(
        to=Service,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=155
    )
    cost = models.PositiveSmallIntegerField(
        verbose_name=_('Cost'),
    )


class GalleryImage(models.Model):
    service = models.ForeignKey(
        to="Service",
        on_delete=models.CASCADE,
        verbose_name=_('Service'),
    )
    image = FilerImageField(
        on_delete=models.CASCADE,
        verbose_name=_('Image')
    )
    
    class Meta:
        verbose_name = _('Service Gallery Image')
        verbose_name_plural = _('Service Gallery Images')


class GalleryVideo(models.Model):
    service = models.ForeignKey(
        to="Service",
        on_delete=models.CASCADE,
        verbose_name=_('Video')
    )
    url = models.URLField(
        verbose_name=_('URL'),
    )
    
    class Meta:
        verbose_name = _('Service Gallery Video')
        verbose_name_plural = _('Service Gallery Videos')

    def save(self, *args, **kwargs):
        url = self.url
        word_to_change = url.replace('watch?v=', 'embed/')
        self.url = word_to_change
        super().save(*args, **kwargs)


class ServiceListPluginModel(CMSPlugin):
    max_count = models.PositiveSmallIntegerField(
        verbose_name=_('Max'),
        help_text=_('How much services to display'),
        default=6
    )


class ServiceRowPluginModel(CMSPlugin):
    display_type = models.CharField(
        max_length=1,
        verbose_name=_('Display type'),
        choices=(('S', 'Simple'),('B', 'Blocks'))
    )
    fetch_from_db = models.BooleanField(
        verbose_name=_('Fetch from db?'),
        default=True
    )
    max_count = models.PositiveSmallIntegerField(
        verbose_name=_('Max'),
        help_text=_('How much services to display'),
        null=True,
        blank=True,
        default=6
    )


class ServicePluginModel(CMSPlugin):
    service = models.ForeignKey(
        to=Service,
        on_delete=models.CASCADE
    )

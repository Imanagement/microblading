from ckeditor.fields import RichTextField
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


class Service(models.Model):
    name = models.CharField(
        verbose_name=_('Название услуги'),
        max_length=555
    )
    slug = models.SlugField(
        verbose_name=_('Slug услуги'),
        unique=True,
        blank=True,
        null=True,
        max_length=555
    )
    header_image = FilerImageField(
        verbose_name=_('Изображение шапки'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='header_image'
    )
    cost = models.PositiveIntegerField(
        verbose_name=_('Цена'),
    )
    cost_name = models.CharField(
        verbose_name=_('Название к цене'),
        max_length=155,
        null=True,
        blank=True
    )
    duration = models.PositiveIntegerField(
        verbose_name=_('Длительность процедуры'),
        default=60
    )
    teaser_description = RichTextField(
        verbose_name=_('Интро текст'),
        help_text=_('Текст который будет описывать услугу на других страницах'),
        null=True,
        blank=True
    )
    description = RichTextField(
        verbose_name=_('Описание'),
        null=True,
        blank=True
    )
    icon = FilerImageField(
        verbose_name=_('Иконка услуги'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='icon'
    )

    what_we_offer_description = RichTextField(
        verbose_name=_('Описание блока "плюсы услуг"'),
        null=True,
        blank=True
    )
    what_we_offer_image = FilerImageField(
        verbose_name=_('Изображение блока "плюсы услуг"'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='what_we_offer_image'
    )
    what_we_offer_video_url = models.URLField(
        max_length=155,
        verbose_name=_('URL видео блока возле цены'),
        null=True,
        blank=True
    )

    # Seo
    h1_title = models.CharField(
        verbose_name=_('H1 Заголовок'),
        max_length=255,
        null=True,
        blank=True
    )
    page_title = models.CharField(
        verbose_name=_('Seo заголовок страницы'),
        max_length=255,
        null=True,
        blank=True
    )
    meta_description = models.TextField(
        verbose_name=_('Мета описание'),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')

    def get_absolute_url(self):
        return reverse('services:service-detail', kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class GalleryImage(models.Model):
    service = models.ForeignKey(
        to="Service",
        on_delete=models.CASCADE,
        verbose_name=_('Услуга'),
    )
    image = FilerImageField(
        on_delete=models.CASCADE,
        verbose_name=_('Изображение')
    )
    
    class Meta:
        verbose_name = _('Изображение для галереи')
        verbose_name_plural = _('Изображения для галереи')


class GalleryVideo(models.Model):
    service = models.ForeignKey(
        to="Service",
        on_delete=models.CASCADE,
        verbose_name=_('Видео')
    )
    url = models.URLField(
        verbose_name=_('URL'),
    )
    
    class Meta:
        verbose_name = _('Видео для галереи')
        verbose_name_plural = _('Видео для галереи')


    def save(self, *args, **kwargs):
        url = self.url
        word_to_change = url.replace('watch?v=', 'embed/')
        self.url = word_to_change
        super().save(*args, **kwargs)

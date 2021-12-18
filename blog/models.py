from djangocms_text_ckeditor.fields import HTMLField
from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField
from re import compile, sub


class Category(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=55
    )
    slug = models.SlugField(
        verbose_name=_('Slug'),
        null=True,
        blank=True
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
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('blog:blog-category-list', kwargs={
            'slug': self.slug
        })

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    category = models.ForeignKey(
        to="Category",
        verbose_name=_('Category'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name=_('Author'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=1

    )
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=155
    )
    slug = models.SlugField(
        verbose_name=_('Slug'),
        null=True,
        blank=True
    )
    image = FilerImageField(
        verbose_name=_('Image'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    body = HTMLField(
        verbose_name=_('Content'),
        null=True,
        blank=True
    )
    created = models.DateTimeField(
        verbose_name=_('Created Date'),
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name=_('Last Update'),
        auto_now=True
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
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('blog:blog-detail', kwargs={
            "slug": self.slug
        })

    def get_teaser_description(self):
        text = self.body
        cleanr = compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        result = sub(cleanr, '', text)
        return f"{result[:355]}[...]"

    def get_next_post(self):
        next_post_id = self.id + 1
        next_post = Post.objects.filter(id=next_post_id).first()
        return reverse('blog:blog-detail', kwargs={
                "slug": next_post.slug
            }) if next_post else 'javascript:void(0)'

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class BlogRecentItemPluginModel(CMSPlugin):
    post = models.ForeignKey(
        to="Post",
        on_delete=models.SET_NULL,
        null=True,
    )
# Generated by Django 3.2.5 on 2021-12-17 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('services', '0003_auto_20211216_1416'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryimage',
            options={'verbose_name': 'Service Gallery Image', 'verbose_name_plural': 'Service Gallery Images'},
        ),
        migrations.AlterModelOptions(
            name='galleryvideo',
            options={'verbose_name': 'Service Gallery Video', 'verbose_name_plural': 'Service Gallery Videos'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
        migrations.RemoveField(
            model_name='service',
            name='what_we_offer_description',
        ),
        migrations.RemoveField(
            model_name='service',
            name='what_we_offer_description_en',
        ),
        migrations.RemoveField(
            model_name='service',
            name='what_we_offer_description_es',
        ),
        migrations.RemoveField(
            model_name='service',
            name='what_we_offer_image',
        ),
        migrations.RemoveField(
            model_name='service',
            name='what_we_offer_video_url',
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service', verbose_name='Service'),
        ),
        migrations.AlterField(
            model_name='galleryvideo',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service', verbose_name='Video'),
        ),
        migrations.AlterField(
            model_name='service',
            name='cost',
            field=models.PositiveIntegerField(verbose_name='Cost'),
        ),
        migrations.AlterField(
            model_name='service',
            name='cost_name',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Cost Title'),
        ),
        migrations.AlterField(
            model_name='service',
            name='cost_name_en',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Cost Title'),
        ),
        migrations.AlterField(
            model_name='service',
            name='cost_name_es',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Cost Title'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description_en',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description_es',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='service',
            name='duration',
            field=models.PositiveIntegerField(default=60, verbose_name='Duration'),
        ),
        migrations.AlterField(
            model_name='service',
            name='h1_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='H1 Title'),
        ),
        migrations.AlterField(
            model_name='service',
            name='h1_title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='H1 Title'),
        ),
        migrations.AlterField(
            model_name='service',
            name='h1_title_es',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='H1 Title'),
        ),
        migrations.AlterField(
            model_name='service',
            name='header_image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='header_image', to=settings.FILER_IMAGE_MODEL, verbose_name='Header Image'),
        ),
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='icon', to=settings.FILER_IMAGE_MODEL, verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='service',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='Meta Description'),
        ),
        migrations.AlterField(
            model_name='service',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta Description'),
        ),
        migrations.AlterField(
            model_name='service',
            name='meta_description_es',
            field=models.TextField(blank=True, null=True, verbose_name='Meta Description'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=555, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name_en',
            field=models.CharField(max_length=555, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name_es',
            field=models.CharField(max_length=555, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='service',
            name='page_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Seo Page Title'),
        ),
        migrations.AlterField(
            model_name='service',
            name='page_title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Seo Page Title'),
        ),
        migrations.AlterField(
            model_name='service',
            name='page_title_es',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Seo Page Title'),
        ),
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, max_length=555, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='service',
            name='slug_en',
            field=models.SlugField(blank=True, max_length=555, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='service',
            name='slug_es',
            field=models.SlugField(blank=True, max_length=555, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='service',
            name='teaser_description',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, help_text='Text which is seen from other pages (Teaser)', null=True, verbose_name='Intro Text'),
        ),
        migrations.AlterField(
            model_name='service',
            name='teaser_description_en',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, help_text='Text which is seen from other pages (Teaser)', null=True, verbose_name='Intro Text'),
        ),
        migrations.AlterField(
            model_name='service',
            name='teaser_description_es',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, help_text='Text which is seen from other pages (Teaser)', null=True, verbose_name='Intro Text'),
        ),
    ]

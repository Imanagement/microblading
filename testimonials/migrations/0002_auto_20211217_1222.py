# Generated by Django 3.2.5 on 2021-12-17 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimonial',
            options={'verbose_name': 'Testimonial', 'verbose_name_plural': 'Testimonials'},
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='image_type',
            field=models.BooleanField(default=True, verbose_name='Testimonial - Image Type?'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='name',
            field=models.CharField(blank=True, max_length=55, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='position',
            field=models.CharField(blank=True, max_length=55, null=True, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='testimonial',
            field=models.TextField(blank=True, null=True, verbose_name='Testimonial'),
        ),
    ]

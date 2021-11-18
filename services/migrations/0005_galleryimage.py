# Generated by Django 3.2.5 on 2021-11-16 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('services', '0004_auto_20210804_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL, verbose_name='Изображение')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service', verbose_name='Услуга')),
            ],
        ),
    ]
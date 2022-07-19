# Generated by Django 3.2.5 on 2021-12-18 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cms', '0023_auto_20211218_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioRowPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='portfolio_portfoliorowpluginmodel', serialize=False, to='cms.cmsplugin')),
                ('fetch_from_db', models.BooleanField(default=True, verbose_name='Fetch from db?')),
                ('stretch', models.BooleanField(default=False, help_text='Full width of screen content', verbose_name='Stretch')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Name')),
                ('image', filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Portfolio Project',
                'verbose_name_plural': 'Portfolio Projects',
            },
        ),
    ]

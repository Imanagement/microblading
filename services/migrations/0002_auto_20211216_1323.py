# Generated by Django 3.2.5 on 2021-12-16 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='what_we_offer_image_en',
        ),
        migrations.RemoveField(
            model_name='service',
            name='what_we_offer_image_es',
        ),
    ]

# Generated by Django 3.2.5 on 2021-12-18 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_auto_20211218_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(blank=True, max_length=575, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description_en',
            field=models.CharField(blank=True, max_length=575, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description_es',
            field=models.CharField(blank=True, max_length=575, null=True, verbose_name='Description'),
        ),
    ]

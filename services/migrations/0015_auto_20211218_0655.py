# Generated by Django 3.2.5 on 2021-12-18 06:55

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_auto_20211218_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='teaser_description',
            field=models.CharField(blank=True, help_text='Text which is seen from other pages (Teaser)', max_length=575, null=True, verbose_name='Intro Text'),
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
    ]

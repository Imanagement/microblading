# Generated by Django 3.2.5 on 2021-11-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_alter_service_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.TextField(max_length=255, verbose_name='Название услуги'),
        ),
    ]

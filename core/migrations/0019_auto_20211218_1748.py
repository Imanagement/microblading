# Generated by Django 3.2.5 on 2021-12-18 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0023_auto_20211216_1029'),
        ('core', '0018_asidenavigationflag_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asidenavigationflag',
            name='navigation_plugin',
        ),
        migrations.DeleteModel(
            name='AsideNavigationPluginModel',
        ),
    ]

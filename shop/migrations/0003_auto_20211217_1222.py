# Generated by Django 3.2.5 on 2021-12-17 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_alter_product_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'Basket', 'verbose_name_plural': 'Baskets'},
        ),
        migrations.AlterModelOptions(
            name='basketproduct',
            options={'verbose_name': 'Basket Product', 'verbose_name_plural': 'Basket Products'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='basket',
            name='basket_changed_date',
            field=models.DateField(blank=True, null=True, verbose_name='Basket Changes Date'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='ordered',
            field=models.BooleanField(default=False, verbose_name='Ordered'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='ordered_date',
            field=models.DateTimeField(verbose_name='Basket Order Date'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='products',
            field=models.ManyToManyField(to='shop.BasketProduct', verbose_name='Products'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Basket Open Date'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='basketproduct',
            name='is_ordered',
            field=models.BooleanField(default=False, verbose_name='Ordered'),
        ),
        migrations.AlterField(
            model_name='basketproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='basketproduct',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Product Count'),
        ),
        migrations.AlterField(
            model_name='basketproduct',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='basketproduct',
            name='which_basket',
            field=models.ManyToManyField(blank=True, to='shop.Basket', verbose_name='Basket'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=djangocms_text_ckeditor.fields.HTMLField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Discount'),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=155, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Cost'),
        ),
        migrations.AlterField(
            model_name='product',
            name='published',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Published Date'),
        ),
    ]

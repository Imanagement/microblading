from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from filer.fields.image import FilerImageField


class Product(models.Model):

    name = models.CharField(
        max_length=155,
        verbose_name=_("Название")
    )
    price = models.IntegerField(
        verbose_name=_("Цена"),
    )
    discount_price = models.IntegerField(
        verbose_name=_("Скидочная цена"),
        null=True,
        blank=True,
        )
    slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=155,
        null=True,
        blank=True,
    )
    description = RichTextUploadingField(
        verbose_name=_('Описание')
    )
    main_image = FilerImageField(
        verbose_name=_('Изображение'),
        on_delete=models.SET_NULL,
        null=True
    )
    published = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации")

    # SEO
    page_title = models.CharField(
        _("Page title"),
        max_length=155,
        null=True,
        blank=True
    )
    meta_description = models.TextField(
        _("Meta Description"),
        null=True,
        blank=True
    )

    related_products = models.ManyToManyField("self")

    def get_absolute_url(self):
        return reverse('')

    class Meta:
        verbose_name = _("Продукт")
        verbose_name_plural = _("Продукты")

    def __str__(self):
        return self.name


class BasketProduct(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Зарегистрированный покупатель')
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Продукт')
    )
    quantity = models.IntegerField(
        default=1,
        verbose_name=_('Количество продукта')
    )
    is_ordered = models.BooleanField(
        default=False,
        verbose_name=_('Заказан')
    )
    which_basket = models.ManyToManyField(
        'Basket',
        blank=True,
        verbose_name=_('Корзина')
    )

    class Meta:
        verbose_name = _("Продукт в корзине")
        verbose_name_plural = _("Продукты в корзинах")

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_summary(self):
        return self.product.price * self.quantity

    def get_total_discount_summary(self):
        return self.product.discount_price * self.quantity


class Basket(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Зарегистрированный покупатель')
    )
    products = models.ManyToManyField(
        BasketProduct,
        verbose_name=_('Продукты')
    )
    start_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата открытия корзины')
    )
    ordered_date = models.DateTimeField(
        verbose_name=_('Дата заказа корзины')
    )
    basket_changed_date = models.DateField(
        verbose_name=_('Дата изменения корзины'),
        null=True,
        blank=True
    )
    ordered = models.BooleanField(
        default=False,
        verbose_name=_('Заказан')
    )

    class Meta:
        verbose_name = _("Корзина")
        verbose_name_plural = _("Корзины")

    def __str__(self):
        if self.user:
            return f"Заказ  #{self.pk} от {self.user}"
        else:
            return f"Заказ(Анонимный) #{self.pk}"

    def get_absolute_url(self):
        return reverse("Order_detail", kwargs={"pk": self.pk})

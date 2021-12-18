from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField


class Product(models.Model):

    name = models.CharField(
        max_length=155,
        verbose_name=_("Name")
    )
    price = models.IntegerField(
        verbose_name=_("Cost"),
    )
    discount_price = models.IntegerField(
        verbose_name=_("Discount"),
        null=True,
        blank=True,
        )
    slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=155,
        null=True,
        blank=True,
    )
    description = HTMLField(
        verbose_name=_('Description')
    )
    main_image = FilerImageField(
        verbose_name=_('Image'),
        on_delete=models.SET_NULL,
        null=True
    )
    published = models.DateTimeField(
        auto_now_add=True, verbose_name="Published Date")

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
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class BasketProduct(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('User')
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Product')
    )
    quantity = models.IntegerField(
        default=1,
        verbose_name=_('Product Count')
    )
    is_ordered = models.BooleanField(
        default=False,
        verbose_name=_('Ordered')
    )
    which_basket = models.ManyToManyField(
        'Basket',
        blank=True,
        verbose_name=_('Basket')
    )

    class Meta:
        verbose_name = _("Basket Product")
        verbose_name_plural = _("Basket Products")

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
        verbose_name=_('User')
    )
    products = models.ManyToManyField(
        BasketProduct,
        verbose_name=_('Products')
    )
    start_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Basket Open Date')
    )
    ordered_date = models.DateTimeField(
        verbose_name=_('Basket Order Date')
    )
    basket_changed_date = models.DateField(
        verbose_name=_('Basket Changes Date'),
        null=True,
        blank=True
    )
    ordered = models.BooleanField(
        default=False,
        verbose_name=_('Ordered')
    )

    class Meta:
        verbose_name = _("Basket")
        verbose_name_plural = _("Baskets")

    def __str__(self):
        if self.user:
            return _(f"Order #{self.pk} from {self.user}")
        else:
            return _(f"Order(Anonymous) #{self.pk}")

    def get_absolute_url(self):
        return reverse("Order_detail", kwargs={"pk": self.pk})

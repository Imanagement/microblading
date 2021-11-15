from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _


class FAQ(models.Model):
    question = models.CharField(
        verbose_name=_('Вопрос'),
        max_length=255
    )
    answer = RichTextField(
        verbose_name=_('Ответ'),
    )

    class Meta:
        verbose_name = _('Часто задаваемый вопрос')
        verbose_name_plural = _('Часто задаваемые вопросы')

    def __str__(self):
        return self.question


class ContactUsModel(models.Model):
    name = models.CharField(
        verbose_name=_('Имя'),
        max_length=55,
    )
    email = models.EmailField(
        verbose_name=_('Email'),
        null=True,
        blank=True
    )
    phone = models.CharField(
        verbose_name=_('Телефон'),
        max_length=35,
    )
    message = models.TextField(
        verbose_name=_('Сообщение'),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Заявка на обратную связь')
        verbose_name_plural = _('Заявки на обратную связь')

    def __str__(self):
        return f"Заявка на обратную связь от {self.name}"

from django import forms
from modeltranslation.forms import TranslationModelForm
from django.utils.translation import gettext_lazy as _

from .models import ContactUsModel


class ContactUsForm(TranslationModelForm):
    class Meta:
        model = ContactUsModel
        fields = ('name', 'email', 'phone', 'message')

    name = forms.CharField(
        max_length=55,
        widget=forms.TextInput(attrs={
            "size": "40",
            "class": "wpcf7-form-control wpcf7-text wpcf7-validates-as-required",
            "placeholder": _("Name")
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "size": "40",
                "class": "wpcf7-form-control wpcf7-text wpcf7-email",
                "placeholder": _("Email")
            })
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "size": "40",
                "class": "wpcf7-form-control wpcf7-text wpcf7-phone",
                "placeholder": _("Phone") + '*'
            })
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "cols": "40",
                "rows": "10,",
                "class": "wpcf7-form-control wpcf7-textarea",
                "placeholder": _("Message")
            })
    )

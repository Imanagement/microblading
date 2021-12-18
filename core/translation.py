from modeltranslation.translator import register, TranslationOptions
from .models import ContactUsModel


@register(ContactUsModel)
class ContactUsModelTranslationOptions(TranslationOptions):
    fields = ('name', 'email', 'phone', 'message')

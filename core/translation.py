from modeltranslation.translator import register, TranslationOptions
from .models import ContactUsModel, FAQ


@register(ContactUsModel)
class ContactUsModelTranslationOptions(TranslationOptions):
    fields = ('name', 'email', 'phone', 'message')


@register(FAQ)
class FAQModelTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')

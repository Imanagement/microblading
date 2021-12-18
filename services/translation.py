from modeltranslation.translator import register, TranslationOptions
from .models import Service


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', 'cost_name', 'description',
              'h1_title', 'page_title', 'meta_description')

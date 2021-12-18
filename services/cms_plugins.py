from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.conf import settings
from django.utils.translation import gettext as _

from .models import Service, ServiceRowPluginModel, ServicePluginModel


@plugin_pool.register_plugin
class ServiceListPluginPublisher(CMSPluginBase):
    module = _('Services')
    name = _('Service List (Only links)')
    render_template = 'services/components/service-list.html'

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context.update({
            'services': Service.objects.all()
        })
        return context


@plugin_pool.register_plugin
class ServiceRowPluginPublisher(CMSPluginBase):
    model = ServiceRowPluginModel
    module = _('Services')
    name = _('Service List (blocks)')
    allow_children = True
    child_classes = ['ServicePluginPublisher']

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        if instance.fetch_from_db:
            context.update({
                'services': Service.objects.all()[:instance.max_count]
            })
        return context

    def get_render_template(self, context, instance, placeholder):
        if instance.display_type == 'S':
            return 'services/components/service-row.html'
        else:
            return 'services/components/pricing-row.html'


@plugin_pool.register_plugin
class ServicePluginPublisher(CMSPluginBase):
    model = ServicePluginModel
    module = _('Services')
    name = _('Service')
    require_parent = True
    parent_classes = ['ServiceRowPluginPublisher']
    render_template = ''

#
# @plugin_pool.register_plugin
# class ServiceNamePlugin(CMSPluginBase):
#     module = _('Services')
#     name = _('Service Name')
#     render_template = 'services/components/service-name.html'
#     text_enabled = True
#
#     def icon_alt(self, instance):
#         return f"{self} - {instance}"
#
#
# @plugin_pool.register_plugin
# class ServiceTeaserDescription(CMSPluginBase):
#     module = _('Services')
#     name = _('Service Teaser')
#     render_template = "services/components/service-teaser-description.html"
#     text_enabled = True
#
#     def render(self, context, instance, placeholder):
#         context = super().render(context, instance, placeholder)
#         print(context['request'])
#         context.update({
#             'teaser_description': Service.objects.filter()[0].teaser_description
#         })
#         return context
#
#     def icon_alt(self, instance):
#         return f"{self} - {instance}"
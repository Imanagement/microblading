from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _

from .models import PortfolioItem, PortfolioRowPluginModel


@plugin_pool.register_plugin
class PortfolioRowPluginPublisher(CMSPluginBase):
    module = _('Projects')
    model = PortfolioRowPluginModel
    name = _('Portfolio Row')
    render_template = 'portfolio/components/gallery-row.html'
    allow_children = True
    child_classes = ['ImagePluginPublisher']

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        if instance.fetch_from_db:
            context.update({
                'portfolio_items': PortfolioItem.objects.all()
            })
        return context

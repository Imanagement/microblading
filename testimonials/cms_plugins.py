from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _

from testimonials.models import Testimonial


@plugin_pool.register_plugin
class TestimonialSliderPluginPublisher(CMSPluginBase):
    module = _('Testimonials')
    name = _('Testimonials slider')
    render_template = 'testimonials/components/testimonial-list.html'

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context.update({
            'testimonials': Testimonial.objects.all()
        })
        return context

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import gettext as _

from .forms import ContactUsForm

from .models import HeaderSectionPluginModel, TitlePluginModel, CounterItemPluginModel, AboutUsBlockPluginModel, \
    ColumnPluginModel, SpacePluginModel, ImagePluginModel, GoogleMapPluginModel, HomeHeaderPluginModel, \
    HomeHeaderAddressModel, RowPluginModel, AnimatedPluginModel, AsideNavigationFlag, SectionPluginModel


@plugin_pool.register_plugin
class AsideNavigationPluginPublisher(CMSPluginBase):
    module = _('Core')
    name = _('Aside Navigation')
    render_template = 'core/components/aside_block.html'
    allow_children = True
    child_classes = ["LinkPlugin"]

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context.update({
            'flags': AsideNavigationFlag.objects.all()
        })
        return context


class AddressInlineAdmin(admin.StackedInline):
    model = HomeHeaderAddressModel
    extra = 1


@plugin_pool.register_plugin  # register the plugin
class HeaderSectionPluginPublisher(CMSPluginBase):
    module = _("Core")
    model = HeaderSectionPluginModel
    name = _("Header")  # name of the plugin in the interface
    render_template = "core/components/page-title.html"
    inlines = (AddressInlineAdmin,)

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        addresses = HomeHeaderAddressModel.objects.all().order_by('id')
        context.update({
            'addresses': addresses,
        })
        return context


@plugin_pool.register_plugin
class HomeHeaderSectionPluginPublisher(CMSPluginBase):
    model = HomeHeaderPluginModel
    module = _('Core')
    name = _('Home header')
    render_template = 'core/components/home-page-title.html'
    inlines = (AddressInlineAdmin,)
    allow_children = True
    child_classes = ['RowPluginPublisher']

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        addresses = HomeHeaderAddressModel.objects.all().order_by('id')
        context.update({
            'addresses': addresses,
        })
        return context


@plugin_pool.register_plugin
class TitlePluginPublisher(CMSPluginBase):
    module = _('Core')
    model = TitlePluginModel
    name = _('Title')
    render_template = 'core/components/title.html'
    allow_children = True
    child_classes = ['TextPlugin']


@plugin_pool.register_plugin
class CounterPluginPublisher(CMSPluginBase):
    module = _('Core')
    name = _('Counter')
    render_template = 'core/components/counter.html'
    allow_children = True
    child_classes = ['CounterItemPluginPublisher']


@plugin_pool.register_plugin
class CounterItemPluginPublisher(CMSPluginBase):
    require_parent = True
    parent_classes = ['CounterPluginPublisher']
    model = CounterItemPluginModel
    name = _('Counter Item')
    render_template = 'core/components/counter-item.html'


@plugin_pool.register_plugin
class AboutUsBlockPluginPublisher(CMSPluginBase):
    model = AboutUsBlockPluginModel
    module = _('Core')
    name = _('About Us Block')
    render_template = 'core/components/about-us-block.html'


@plugin_pool.register_plugin
class SectionPluginPublisher(CMSPluginBase):
    module = _('Layout')
    model = SectionPluginModel
    name = _('Section')
    render_template = 'core/components/layout/section.html'
    allow_children = True


@plugin_pool.register_plugin
class RowPluginPublisher(CMSPluginBase):
    model = RowPluginModel
    module = _('Layout')
    name = _('Row')
    render_template = 'core/components/layout/row.html'
    allow_children = True
    child_classes = ['ColumnPluginPublisher']


@plugin_pool.register_plugin
class ColumnPluginPublisher(CMSPluginBase):
    model = ColumnPluginModel
    name = _('Column')
    require_parent = True
    parent_classes = ['RowPluginPublisher']
    render_template = 'core/components/layout/column.html'
    allow_children = True


@plugin_pool.register_plugin
class SpacePluginPublisher(CMSPluginBase):
    model = SpacePluginModel
    name = _('Space')
    module = _('Layout')
    render_template = 'core/components/layout/space.html'


@plugin_pool.register_plugin
class ImagePluginPublisher(CMSPluginBase):
    model = ImagePluginModel
    module = _('Core')
    name = _('Image')
    render_template = 'core/components/image.html'


@plugin_pool.register_plugin
class SocialsPluginPublisher(CMSPluginBase):
    module = _('Core')
    name = _('Socials')
    render_template = 'core/components/socials.html'
    allow_children = True
    child_classes = ['LinkPlugin']


@plugin_pool.register_plugin
class SliderPluginPublisher(CMSPluginBase):
    module = _('Core')
    name = _('Slider')
    render_template = 'core/components/slider.html'
    allow_children = True
    child_classes = ['ImagePluginPublisher']


@plugin_pool.register_plugin
class GoogleMapPluginPublisher(CMSPluginBase):
    module = _('Core')
    model = GoogleMapPluginModel
    name = _('Google map')
    render_template = 'core/components/google-map.html'


@plugin_pool.register_plugin
class ContactUsFormPluginPublisher(CMSPluginBase):
    module = _('Core')
    name = _('Contact form')
    render_template = 'core/components/contact-us-form.html'

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context.update({
            'form': ContactUsForm()
        })
        return context


@plugin_pool.register_plugin
class AnimatedPluginPublisher(CMSPluginBase):
    model = AnimatedPluginModel
    module = _('Core')
    name = _('Animated')
    render_template = 'core/components/text.html'
    allow_children = True



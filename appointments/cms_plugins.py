from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _


@plugin_pool.register_plugin  # register the plugin
class AppointmentSectionPluginPublisher(CMSPluginBase):
    module = _("Appointments")
    name = _("Appointment Section")  # name of the plugin in the interface
    render_template = "appointments/appointment.html"

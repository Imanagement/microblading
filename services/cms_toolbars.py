from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.utils.urlutils import admin_reverse
from django.utils.translation import gettext as _


@toolbar_pool.register
class ServicesToolbarClass(CMSToolbar):
    supported_apps = ['services']

    def populate(self):

        self.toolbar.add_modal_item(
            name=_('Service List'),
            url=admin_reverse('services_service_changelist')
            )

        self.toolbar.add_modal_button(
            name=_('Add Service'),
            url=admin_reverse('services_service_add')
        )

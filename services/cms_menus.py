from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool

from .models import Service


class ServiceMenu(CMSAttachMenu):
    name = _("Service Menu")  # give the menu a name this is required.

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []
        for service in Service.objects.all():
            node = NavigationNode(
                title=service.name,
                url=reverse('services:service-detail', args={service.slug}),
                id=service.pk,  # unique id for this node within the menu
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(ServiceMenu)

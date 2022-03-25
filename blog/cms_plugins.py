from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _

from .models import BlogRecentItemPluginModel


@plugin_pool.register_plugin  # register the plugin
class BlogRecentSectionPluginPublisher(CMSPluginBase):
    module = _("Blog")
    name = _("Recent Blog Posts")  # name of the plugin in the interface
    render_template = "blog/components/recent-posts.html"
    child_classes = ['BlogRecentItemPluginPublisher']
    allow_children = True


@plugin_pool.register_plugin
class BlogRecentItemPluginPublisher(CMSPluginBase):
    module = _("Blog")
    model = BlogRecentItemPluginModel
    name = _("Recent Post")
    render_template = "blog/components/recent-posts-item.html"
    require_parent = True
    allow_children = False
    parent_classes = ["BlogRecentSectionPluginPublisher"]

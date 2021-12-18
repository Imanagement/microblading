from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class ServicesApphook(CMSApp):
    app_name = "services"  # must match the application namespace
    name = "Services"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["services.urls"] # replace this with the path to your application's URLs module

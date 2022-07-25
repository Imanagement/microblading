"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, re_path
from django.conf.urls.i18n import i18n_patterns
from core.services.urlresolvers import solid_i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

admin.autodiscover()

urlpatterns = solid_i18n_patterns(
    re_path(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    prefix_default_language=False
)

urlpatterns += solid_i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('cms.urls')),
    path('core', include('core.urls')),
    prefix_default_language=False
    # path('services/', include('services.urls')),
    # path('gallery/', include('portfolio.urls')),
    # path('blog/', include('blog.urls'))
)

if settings.DEBUG:
    urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


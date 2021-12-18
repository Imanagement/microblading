from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from services.views import service_list, service_detail

app_name = 'services'
urlpatterns = [
    path('', service_list, name="service-list"),
    path('<slug>', service_detail, name="service-detail"),
]

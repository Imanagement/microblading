from django.urls import path
from .views import contact_us_view


def dummy():
    pass


app_name = 'core'
urlpatterns = [
    path('contact-us', contact_us_view, name="contact-us"),
    path('search', dummy, name="search")
]

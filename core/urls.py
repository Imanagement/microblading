from django.urls import path
from .views import index, contact_us_view, about_us_view, search_view

app_name = 'core'
urlpatterns = [
    path('', index, name="index"),
    path('about-us', about_us_view, name='about-us'),
    path('contact-us', contact_us_view, name='contact-us'),
    path('search', search_view, name="search")
]

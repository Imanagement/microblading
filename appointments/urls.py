from django.urls import path
from .views import index


app_name = 'appointments'
urlpatterns = [
    path('', index, 'appointment-index')
]
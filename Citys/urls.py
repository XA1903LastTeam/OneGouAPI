from django.urls import path

from .views import get_city

app_name = 'city'


urlpatterns = [
    path('get_city/',get_city,name='city')
]
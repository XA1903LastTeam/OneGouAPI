from django.urls import path

from .views import CityApi

app_name = 'city'


urlpatterns = [
    path('get_city/',CityApi.as_view(),name='city')
]
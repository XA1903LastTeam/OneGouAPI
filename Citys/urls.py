from django.urls import path

from .views import CityApi,CityAreaApi

app_name = 'city'


urlpatterns = [
    path('get_city/',CityApi.as_view(),name='city'),
    path('get_city/area',CityAreaApi.as_view(),name='area')
]
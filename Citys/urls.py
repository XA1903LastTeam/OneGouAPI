from django.urls import path

from .views import CityApi,CityAreaApi

app_name = 'city'


urlpatterns = [
    path('all/',CityApi.as_view(),name='city'),
    path('area/',CityAreaApi.as_view(),name='area')
]
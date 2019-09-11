# -*- coding: utf-8 -*-
from django.urls import path
from .views import *

app_name = 'goods_app'

urlpatterns = [
    path('home/', GetHomeDataView.as_view(), name='get_home')
]

from django.urls import path

from UserApp.views import UserAPIView

app_name = 'order_info'

urlpatterns = [
    path('list/',UserAPIView.as_view(), name='list'),
]

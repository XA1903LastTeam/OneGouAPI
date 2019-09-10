from django.urls import path

from UserApp.views import UserAPIView

app_name = 'user_app'

urlpatterns = [
    path('list/',UserAPIView.as_view(), name='list'),
]

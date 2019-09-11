from django.urls import path
from .tool import new_img_code
from UserApp.views import UserAPIView

app_name = 'user_app'

urlpatterns = [
    path('list/',UserAPIView.as_view(), name='list'),
    path('yzm/', new_img_code, name='yzm')
]


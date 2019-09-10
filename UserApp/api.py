# 用户API接口

from rest_framework import serializers, viewsets
from rest_framework import routers
from .models import UserModel

class UserSeraLizer(serializers):
    class Meta:
        model = UserModel
        fields = ('id', 'name', 'phone', 'image', 'sex', 'bool', 'address_id')


class UserAPIView(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSeraLizer


# 声明API路由
api_router = routers.DefaultRouter()

api_router.register('user', UserAPIView)
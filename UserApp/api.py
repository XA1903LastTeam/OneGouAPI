# 用户API接口

from rest_framework import serializers
from .models import UserModel

class UserSeraLizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'name', 'phone', 'image', 'sex', 'bool', 'address_id')


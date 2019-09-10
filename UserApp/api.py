# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import NavModel

#
# class NavSerrializer(serializers.Serializer):
#     nav_child_id = NavModel.nav_child_id.goods_cate__set.objects.all()
#
#     class Meta:
#         model = NavModel
#         fields = ['id', 'nav_child_id', 'name', 'image']


# 用户API接口

from .models import UserModel


class UserSeraLizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'name', 'phone', 'image', 'sex', 'bool', 'address_id')

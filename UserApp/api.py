# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import NavModel


class NavSerrializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NavModel
        fields = ['id', 'nav_child_id', 'name', 'image']


# 用户API接口

from .models import UserModel
from Address.models import AddressModel


class UserSeraLizer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'name', 'phone', 'image', 'sex', 'bool', 'address_id')

<<<<<<< HEAD
=======

class AdderssSeraLizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddressModel
        fields = ('id', 'address')
>>>>>>> 57b859ac59c4c116f344f6f190f4ebd3e9b0b437

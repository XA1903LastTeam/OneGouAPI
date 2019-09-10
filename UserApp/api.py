# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import NavModel

class NavSerrializer(serializers.Serializer):
    nav_child_id = NavModel.nav_child_id.goods_cate.objects.all()
    class Meta:
        model = NavModel
        fields = ['id', 'nav_child_id', 'name', 'image']
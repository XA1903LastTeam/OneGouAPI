# -*- coding: utf-8 -*-
from .models import SiwapModel, GoodsInfoModel, GoodsModel
from rest_framework import serializers
from Address.api import ActiveSerializer
from Funy.api import CategoryModelSerializers


class GoodsModelSerializers(serializers.ModelSerializer):
    categoryid = CategoryModelSerializers

    class Meta:
        model = GoodsModel
        fields = ['commodityname', 'commoditycode', 'maxlimitcount', 'originalprice', 'goodshot']


class SiwapModelSerializers(serializers.ModelSerializer):
    active_id = ActiveSerializer

    class Meta:
        model = SiwapModel
        fields = ['active_id', 'active_img']


class GoodsInfoModelSerializers(serializers.ModelSerializer):
    goods_id = GoodsModelSerializers

    class Meta:
        model = GoodsInfoModel
        fields = ['commodityinfo', 'sellprice', 'subtitle', 'spec', 'placeoforgin']

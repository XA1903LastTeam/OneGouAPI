# -*- coding: utf-8 -*-
from .models import SiwapModel, GoodsInfoModel, GoodsModel, GoodsImageModel
from rest_framework import serializers
from Address.api import ActiveSerializer
from Funy.api import CategoryModelSerializers


class GoodsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsImageModel
        fields = ['id', 'img1']


class GoodsModelSerializers(serializers.ModelSerializer):
    categoryid = CategoryModelSerializers
    image = GoodsImageSerializers(many=True)

    class Meta:
        model = GoodsModel
        fields = ['commodityname', 'commoditycode', 'maxlimitcount', 'originalprice', 'goodshot', 'info_id', 'image']


class SiwapModelSerializers(serializers.ModelSerializer):
    active_id = ActiveSerializer

    class Meta:
        model = SiwapModel
        fields = ['active_id', 'active_img']


class GoodsInfoModelSerializers(serializers.ModelSerializer):
    goods_id = GoodsModelSerializers()

    class Meta:
        model = GoodsInfoModel
        fields = ['commodityinfo', 'sellprice', 'subtitle', 'spec', 'placeoforgin', 'unit', 'goods_id']

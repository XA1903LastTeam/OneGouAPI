# 订单详情API
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Order_listModel


class Order_listSeraLizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order_listModel
        fields = ('id', 'order_id', 'start_time', 'order_statud', 'goods_id', 'count', 'address_id', 'count_price')


class CartModelSeralizer(serializers.ModelSerializer):
    pass

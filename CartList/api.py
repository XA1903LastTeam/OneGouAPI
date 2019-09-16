# 订单详情API
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Order_listModel, CartModel
from UserApp.api import UserSeraLizer


class Order_listSeraLizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order_listModel
        fields = ('id', 'order_id', 'start_time', 'order_statud', 'goods_id', 'count', 'address_id', 'count_price')


class Order_list_1_SeraLier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order_listModel
        fields = ('count',)


class CartModelSeralizer(serializers.ModelSerializer):
    user_id = UserSeraLizer()

    class Meta:
        model = CartModel
        fields = ('id',)

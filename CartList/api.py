# 订单详情API
from rest_framework import serializers

from UserApp.api import AdderssSeraLizer
from .models import Order_listModel


class Order_listSeraLizer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order_listModel
        fields = ('id', 'start_time', 'order_statud')


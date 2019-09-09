from django.db import models

# Create your models here.
from django.db import models
from common import YGBaseModel


class CartModel(YGBaseModel):
    user_id = models.OneToOneField('UserApp.UserModel', on_delete=models.CASCADE, verbose_name='用户ID')

    def __str__(self):
        return self.user_id


class OrderModel(YGBaseModel):
    user_id = models.IntegerField(verbose_name='用户ID')


class Order_listModel(YGBaseModel):
    order_id = models.OneToOneField('CartList.OrderModel', on_delete=models.CASCADE, verbose_name='订单ID')
    start_time = models.CharField(max_length=50, verbose_name='下单时间')
    order_statud = models.IntegerField(choices=((0, '待支付'), (1, '已支付'), (2, '已取消'), (3, '待发货'), (4, '已发货'), (5, '已完成')),
                                       verbose_name='订单状态')
    goods_id = models.ManyToManyField('Goods.GoodsModel', related_name='goods', db_table='t_goods_order_list',
                                      verbose_name='商品ID')
    count = models.IntegerField(verbose_name='商品数量')

    card_id = models.IntegerField(verbose_name='所属购物车')

    def __str__(self):
        return self.order_id

    @property
    def count_price(self):
        return self.goods_id.originalprice * self.count

from django.db import models

# Create your models here.
from django.db import models
from common import YGBaseModel


class CartModel(YGBaseModel):
    user_id = models.OneToOneField('UserApp.UserModel',
                                   on_delete=models.CASCADE,
                                   verbose_name='用户ID',
                                   related_name='user')

    def __str__(self):
        return self.user_id_id

    class Meta:
        db_table = 't_cart'
        verbose_name_plural = verbose_name = '购物车表'


class OrderModel(YGBaseModel):
    user_id = models.ForeignKey('UserApp.UserModel', on_delete=models.CASCADE, verbose_name='用户订单ID',
                                related_name='user_order')
    card_id = models.ForeignKey('CartList.CartModel',
                                verbose_name='所属购物车',
                                related_name='orders',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 't_order'
        verbose_name_plural = verbose_name = '订单表'


class Order_listModel(YGBaseModel):
    order_id = models.OneToOneField('CartList.OrderModel',
                                    on_delete=models.CASCADE,
                                    verbose_name='订单ID',
                                    related_name='order')
    start_time = models.CharField(max_length=50, verbose_name='下单时间')
    order_statud = models.IntegerField(choices=((0, '待支付'),
                                                (1, '已支付'),
                                                (2, '已取消'),
                                                (3, '待发货'),
                                                (4, '已发货'),
                                                (5, '已完成')),
                                       verbose_name='订单状态')
    goods_id = models.ManyToManyField('Goods.GoodsModel', related_name='goods', db_table='t_goods_order_list',
                                      verbose_name='商品ID')
    count = models.IntegerField(verbose_name='商品数量')

    addr_id = models.ForeignKey('Address.AddressModel', on_delete=models.CASCADE, verbose_name='订单地址',
                                related_name='addrs')

    def __str__(self):
        return self.order_id_id

    @property
    def count_price(self):
        return self.goods_id.originalprice * self.count

    class Meta:
        db_table = 't_orderlist'
        verbose_name_plural = verbose_name = '订单详情表'

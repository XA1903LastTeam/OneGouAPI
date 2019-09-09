from django.db import models
from common import YGBaseModel


class cartModel(YGBaseModel):
    user_id = models.OneToOneField('', on_delete=models.CASCADE, verbose_name='用户ID')

    def __str__(self):
        return self.user_id


class orderModel(YGBaseModel):
    user_id = models.IntegerField(max_length=50, verbose_name='用户ID')


class order_listModel(YGBaseModel):
    order_id = models.OneToOneField('', on_delete=models.CASCADE, verbose_name='订单ID')
    start_time = models.DateTimeField(max_length=50, verbose_name='下单时间')
    order_statud = models.IntegerField(choices=((0, '待支付'), (1, '已支付'), (2, '已取消'), (3, '待发货'), (4, '已发货'), (5, '已完成')),
                                       verbose_name='订单状态')
    goods_id = models.ManyToManyField('', related_name='goods', db_table='t_goods_order_list', verbose_name='商品ID')
    count = models.IntegerField(max_length=50, verbose_name='商品数量')

    card_id = models.IntegerField(max_length=50, verbose_name='所属购物车')

    def __str__(self):
        return self.order_id

    @property
    def count_price(self):
        return self.goods_id.originalprice * self.count


# Create your models here.

from common import YGBaseModel


class CategoryModel(YGBaseModel):
    name = models.CharField(max_length=10, verbose_name='分类名')
    category_url = models.CharField(max_length=200, verbose_name='分类图片')
    father_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='父分类名',
                                  related_name='category')

    class Meta:
        db_table = 't_category'
        verbose_name_plural = verbose_name = '分类表'


class YgeatModel(YGBaseModel):
    eat_img = models.CharField(max_length=200, verbose_name='图片地址')
    eat_content = models.CharField(max_length=50, verbose_name='描述')
    eat_time = models.CharField(max_length=20, verbose_name='时间')
    hot = models.IntegerField(verbose_name='热度')

    class Meta:
        db_table = 't_ygeat'
        verbose_name_plural = verbose_name = '吃喝玩乐'

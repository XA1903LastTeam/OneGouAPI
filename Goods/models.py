from django.db import models
from common import YGBaseModel


# Create your models here.
# 商品表
class GoodsModel(YGBaseModel):
    class Meta:
        db_table = 't_goods'
        verbose_name_plural = verbose_name = '商品表'

    categoryid = models.ForeignKey('',
                                   verbose_name='所属分类',
                                   related_name='goods',
                                   on_delete=models.SET_NULL)
    commodityname = models.CharField(max_length=20,
                                     verbose_name='商品名')
    commoditycode = models.IntegerField(verbose_name='编号')
    maxlimitcount = models.IntegerField(verbose_name='最大购买数')
    originalprice = models.DecimalField(verbose_name='原价',
                                        max_digits=2,
                                        max_length=10)
    goodshot = models.IntegerField(verbose_name='热度')

    def __str__(self):
        return self.commodityname


# 标签名
class TagModel(YGBaseModel):
    class Meta:
        db_table = 't_tag'
        verbose_name_plural = verbose_name = '标签表'

    tag = models.CharField(max_length=100, verbose_name='标签')


# 商品详情表
class GoodsInfoModel(YGBaseModel):
    class Meta:
        db_table = 't_goods_info'
        verbose_name_plural = verbose_name = '商品详情表'

    goods_id = models.OneToOneField(GoodsModel,
                                    on_delete=models.CASCADE,
                                    related_name='goods',
                                    verbose_name='商品id')
    commodityinfo = models.CharField(max_length=50,
                                     verbose_name='商品说明')
    sellprice = models.FloatField(verbose_name='折扣价')
    subtitle = models.CharField(max_length=20,
                                verbose_name='副标题')
    promotiontag = models.ManyToManyField(TagModel,
                                          db_table='goods_info_tag',
                                          related_name='goodsinfo',
                                          verbose_name='标签名')
    commoditunit = models.CharField(max_length=20,
                                    verbose_name='单位')
    commdityspec = models.CharField(max_length=20,
                                    verbose_name='规格')
    video = models.CharField(max_length=200,
                             verbose_name='视频')
    placeoforgin = models.CharField(max_length=100,
                                    verbose_name='产地')

    def __str__(self):
        return self.goods_id.commodityname

    @property
    def commdity_spec_unit(self):
        return self.commoditunit + '/' + self.commdityspec


# 轮播图表
class SiwapModel(YGBaseModel):
    class Meta:
        db_table = 't_siwap'
        verbose_name_plural = verbose_name = '轮播图表'

    active_id = models.OneToOneField('',
                                     on_delete=models.CASCADE,
                                     related_name='actives',
                                     verbose_name='活动表')
    active_img = models.CharField(max_length=200,
                                  verbose_name='活动大图')

    def __str__(self):
        pass

# 商品图片表
class GoodsImageModel(YGBaseModel):
    class Meta:
        db_table = 't_goods_image'
        verbose_name_plural = verbose_name = '商品图片'

    img1 = models.CharField(max_length=200,
                            verbose_name='商品图片')

    goods_id = models.ForeignKey(GoodsModel,
                                 on_delete=models.SET_NULL,
                                 related_name='goods',
                                 verbose_name='商品id')

    def __str__(self):
        return self.goods_id.commodityname
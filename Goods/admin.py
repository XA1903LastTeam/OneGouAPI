from django.contrib import admin
from .models import TagModel, GoodsImageModel, SiwapModel, GoodsModel, GoodsInfoModel


# Register your models here.
class GoodsModelAdmin(admin.ModelAdmin):
    list_display = ('categoryid', 'commodityname', 'commoditycode', 'maxlimitcount', 'originalprice', 'goodshot')


class TagModelAdmin(admin.ModelAdmin):
    list_display = ('tag',)


class GoodsInfoModelAdmin(admin.ModelAdmin):
    list_display = (
        'goods_id', 'sellprice', 'placeoforgin', 'get_name')

    def get_name(self, obj):
        return obj.commdity_spec_unit

    get_name.short_description = '规格'


class SiwapModelAdmin(admin.ModelAdmin):
    list_display = ('active_id', 'active_img')


class GoodsImageModelAdmin(admin.ModelAdmin):
    list_display = ('img1', 'goods_id')


admin.site.register(GoodsModel, GoodsModelAdmin)
admin.site.register(GoodsInfoModel, GoodsInfoModelAdmin)
admin.site.register(TagModel, TagModelAdmin)
admin.site.register(SiwapModel, SiwapModelAdmin)
admin.site.register(GoodsImageModel, GoodsImageModelAdmin)

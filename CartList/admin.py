from django.contrib import admin
from .models import OrderModel, Order_listModel, CartModel


# Register your models here.
class CartModelAdmin(admin.ModelAdmin):
    list_display = ('user_id',)
    fields = ('user_id',)


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('user_id','card_id')
    fields = ('user_id','card_id')


class OrderListModelAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'start_time', 'order_statud', 'count', 'addr_id')
    fields = ('order_id', 'start_time', 'order_statud', 'count','addr_id')


admin.site.register(CartModel, CartModelAdmin)
admin.site.register(OrderModel, OrderModelAdmin)
admin.site.register(Order_listModel, OrderListModelAdmin)

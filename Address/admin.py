from django.contrib import admin

# Register your models here.
from Address.models import AddressModel, DiscountModel


class AddressModelAdmin(admin.ModelAdmin):
    list_display = ('address', 'user_id')
    fields = ('address', 'user_id')


class DiscountModelAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'deduction', 'total', 'datatime', 'periode_of_validity')
    fields = ('user_id', 'deduction', 'total', 'datatime', 'periode_of_validity')


admin.site.register(AddressModel, AddressModelAdmin)
admin.site.register(DiscountModel, DiscountModelAdmin)

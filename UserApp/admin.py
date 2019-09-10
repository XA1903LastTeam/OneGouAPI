from django.contrib import admin

# Register your models here.
from UserApp.models import UserModel, CommentsModel, NavModel


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'image', 'sex', 'bool')
    fields = ('name', 'phone', 'image', 'sex', 'bool')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'comments', 'comment_time')
    fields = ('order_id', 'comments', 'comment_time')


class NavModelAdmin(admin.ModelAdmin):
    list_display = ('nav_child_id', 'name', 'image')
    fields = ('nav_child_id', 'name', 'image')

admin.site.register(UserModel, UserModelAdmin)
admin.site.register(CommentsModel, CommentsAdmin)
admin.site.register(NavModel, NavModelAdmin)

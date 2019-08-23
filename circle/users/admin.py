from django.contrib import admin
from django.utils.safestring import mark_safe
from users import models


@admin.register(models.Auth)
class Users(admin.ModelAdmin):
    list_display = ('id', 'header', 'username', 'email', 'phone', 'is_active', 'is_staff')
    list_per_page = 10
    ordering = ('id', )
    list_editable = ['is_active', 'is_staff']
    list_display_links = ('username', )
    list_filter = ('date_joined', )  # 过滤器
    search_fields = ('username', 'email', 'phone',)  # 搜索字段

    def header(self, obj):
        return mark_safe('<img src="/%s" width="30px" />' % obj.head)
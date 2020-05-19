from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, UserProfile, UserAddress


@admin.register(User)
class UserAdmin(UserAdmin):
    # fields = ('integral', 'level', 'nickname')
    list_display = ('format_username', 'nickname', 'integral', 'is_active')
    search_fields = ('username', 'nickname')
    actions = ['disable_user', 'enable_user']  # 添加自定义方法
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'integral', 'nickname')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def format_username(self, obj):
        return obj.username[0:3] + "***"
    format_username.short_description = '用户名'


    def disable_user(self, request, queryset):
        queryset.update(is_active=False)
    disable_user.short_description = '批量禁用用户'

    def enable_user(self, request, queryset):
        queryset.update(is_active=True)
    enable_user.short_description = '批量启用用户'

# admin.site.register(User, UserAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_no', 'sex')

@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'province', 'city', 'username', 'address', 'phone', 'is_valid', 'is_default')
    search_fields = ('user__username', 'user__nickname', 'phone', 'username')


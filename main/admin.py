from django.contrib import admin

from .models import AppInfo, LoginPasswordInfo

# Register your models here.
@admin.register(AppInfo)
class AppInfoAdmin(admin.ModelAdmin):
    list_display = ('name_app', 'user')
    ordering = ('name_app', 'user')
    search_fields = ('name_app', 'user__username')

@admin.register(LoginPasswordInfo)
class LoginPasswordInfoAdmin(admin.ModelAdmin):
    list_display = ('appinfo', 'login')
    ordering = ('appinfo',)
    search_fields = ('appinfo__name_app',)
from django.contrib import admin

# Register your models here.
from .models import APISettings
from django.contrib.auth.models import User

admin.site.site_header = "Nairobi Stock Exchange"
admin.site.site_title = "Nairobi Stock Exchange"
admin.site.index_title = "Nairobi Stock Exchange"
admin.AdminSite.index_title="STOCK PREDICTION SYSTEM"


class APISettingAdmin(admin.ModelAdmin):

    # fields to be displayed on search box
    search_fields = ('id', 'api_name',)

    # columns to be displayed on listing view

    list_display = ('api_name', 'api_key', 'api_username', 'api_password', 'api_endpoint')


class UserAdmin(admin.ModelAdmin):

    # fields to be displayed on search box
    search_fields = ('id',)

    # columns to be displayed on listing view

    # list_display = ('email', 'api_key', 'api_username', 'api_password', 'api_endpoint')


admin.site.register(APISettings, APISettingAdmin)



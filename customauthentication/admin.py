from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserAuthentication

class CustomUserAdmin(UserAdmin):
    model = CustomUserAuthentication
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets
    ordering = ('email',)


admin.site.register(CustomUserAuthentication, CustomUserAdmin)
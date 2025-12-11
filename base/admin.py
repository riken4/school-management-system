from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from .models import School_Class, herosection, Student


class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'name', 'address', 'roll_number', 'enrollment_date', 'image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('User Type', {'fields': ('user_type',)}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'is_staff')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(School_Class)
admin.site.register(herosection)
admin.site.register(Student)
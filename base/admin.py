from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import School_Class


admin.site.register(School_Class)
admin.site.register(CustomUser)

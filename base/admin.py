from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import School_Class, herosection, Student


admin.site.register(School_Class)
admin.site.register(CustomUser)
admin.site.register(herosection)
admin.site.register(Student)
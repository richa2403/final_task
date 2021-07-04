from Task_App.models import AdminSuper, UserMin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserModel(UserAdmin):
    pass


admin.site.register(AdminSuper)
admin.site.register(UserMin)
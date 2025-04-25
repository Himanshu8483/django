from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(BaseInfo)
admin.site.register(ProxyBaseInfo)

@admin.register(BaseInfo)
class BaseFieldAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'address', 'branch', 'fees']
from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(BaseField)
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Client)

@admin.register(BaseField)
class BaseFieldAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'contact']
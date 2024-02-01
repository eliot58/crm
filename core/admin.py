from django.contrib import admin
from .models import *

class LogInline(admin.StackedInline):
    model = Log
    extra = 1

@admin.register(Client)
class DriverAdmin(admin.ModelAdmin):
    inlines = [LogInline]
    list_display = ['name_point', 'fullName', 'address', 'region', 'director_phone', 'manager_phone', 'email', 'with_work', 'is_potential']
from django.contrib import admin

from .models import States

@admin.register(States)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'population', 'region')

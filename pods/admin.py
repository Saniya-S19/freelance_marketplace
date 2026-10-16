from django.contrib import admin
from .models import Pod

@admin.register(Pod)
class PodAdmin(admin.ModelAdmin):
    list_display = ('name', 'captain', 'created_at')
    search_fields = ('name', 'description', 'captain__username')
    filter_horizontal = ('members',)
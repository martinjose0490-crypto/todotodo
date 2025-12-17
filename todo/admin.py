from django.contrib import admin
from .models import TodoItem

@admin.register(TodoItem)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('subject', 'created_at')
    search_fields = ('subject',)
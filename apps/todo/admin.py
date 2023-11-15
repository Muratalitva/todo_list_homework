from django.contrib import admin

from apps.todo.models import Task
# Register your models here.
@admin.register(Task)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_completed', 'created_at')
    search_fields =  ('title', 'description', 'is_completed', 'created_at')

from django.contrib import admin

# Register your models here.
from users.models import User
# Register your models here.
@admin.register(User)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'created_at', 'age')
    search_fields = ('username', 'email', 'phone_number', 'created_at', 'age')
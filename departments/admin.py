from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_of_department', 'status', 'created_at')
    list_filter = ('status', 'head_of_department', 'created_at')
    search_fields = ('name', 'head_of_department', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)

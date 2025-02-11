from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'group', 'status', 'grade', 'gender', 'parent_name', 'created_at')
    list_filter = ('status', 'grade', 'gender', 'group')
    search_fields = ('first_name', 'last_name', 'parent_name', 'group__group_name')
    ordering = ('last_name', 'first_name')

from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'department', 'subject', 'employment_type', 'status', 'join_date')
    list_filter = ('status', 'employment_type', 'department', 'subject')
    search_fields = ('first_name', 'last_name', 'department__department_name', 'subject__subject_name')
    ordering = ('first_name',)

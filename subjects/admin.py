from django.contrib import admin
from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'credit_hours', 'grade_level', 'status', 'department', 'created_at')
    list_filter = ('status', 'grade_level', 'department')
    search_fields = ('subject_name', 'department__department_name')
    ordering = ('subject_name',)

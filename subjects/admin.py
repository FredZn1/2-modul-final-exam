from django.contrib import admin
from .models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'credit_hours', 'grade_level', 'status')
    list_filter = ('department', 'grade_level', 'status')
    search_fields = ('name', 'department__name', 'teachers__first_name', 'teachers__last_name')
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('teachers',)

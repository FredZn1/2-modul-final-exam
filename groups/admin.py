from django.contrib import admin
from .models import Group

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'grade_level', 'status', 'schedule', 'max_students', 'teacher')  # Ko‘rinadigan ustunlar
    list_filter = ('grade_level', 'status', 'schedule')
    search_fields = ('group_name', 'teacher__full_name', 'academic_year')
    prepopulated_fields = {'slug': ('group_name',)}
    ordering = ('grade_level', 'group_name')
    filter_horizontal = ('subjects',)
    autocomplete_fields = ('teacher',)

from django.contrib import admin
from .models import Group

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade_level', 'schedule', 'teacher', 'academic_year', 'status')
    list_filter = ('grade_level', 'schedule', 'status')
    search_fields = ('name', 'teacher__name', 'academic_year')
    prepopulated_fields = {'slug': ('name',)}


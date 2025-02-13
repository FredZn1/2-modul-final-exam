from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'group', 'grade', 'status')
    list_filter = ('grade', 'status', 'gender')
    search_fields = ('first_name', 'last_name', 'email', 'group__name')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}

from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'department', 'employment_type', 'status')
    list_filter = ('department', 'employment_type', 'status')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}

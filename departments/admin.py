from django.contrib import admin
from .models import Department, HeadOfDepartment


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'head_of_department', 'status', 'contact_email', 'contact_phone')
    search_fields = ('department_name', 'head_of_department__full_name')
    prepopulated_fields = {'slug': ('department_name',)}


@admin.register(HeadOfDepartment)
class HeadOfDepartmentAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

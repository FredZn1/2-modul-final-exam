from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from config.utils import BaseModel


class HeadOfDepartment(models.Model):
    HEAD_CHOICES = [
        ('John Smith', 'John Smith'),
        ('Alice Johnson', 'Alice Johnson'),
        ('Robert Brown', 'Robert Brown'),
        ('Emma Davis', 'Emma Davis'),
        ('Michael Wilson', 'Michael Wilson'),
        ('Sarah Taylor', 'Sarah Taylor'),
        ('David Martinez', 'David Martinez'),
        ('Olivia Anderson', 'Olivia Anderson'),
        ('James Thomas', 'James Thomas'),
        ('Laura White', 'Laura White'),
    ]

    full_name = models.CharField(max_length=100, choices=HEAD_CHOICES, unique=True)

    def __str__(self):
        return self.full_name


class Department(BaseModel):
    STATUS_CHOICES = [
        ('a', 'Active'),
        ('i', 'Inactive'),
        ('c', 'Closed'),
    ]

    department_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    head_of_department = models.ForeignKey(HeadOfDepartment, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='a')
    description = models.TextField(blank=True, null=True)
    location = models.TextField()
    contact_email = models.EmailField(unique=True)
    contact_phone = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.department_name)
        super().save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('departments:detail', args=[self.slug])

    def get_update_url(self):
        return reverse('departments:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('departments:delete', args=[self.pk])

    def __str__(self):
        return f"{self.department_name} - {self.get_status_display()}"

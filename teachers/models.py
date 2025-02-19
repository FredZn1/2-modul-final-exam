from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from config.utils import BaseModel
from departments.models import Department
from django.conf import settings

class Teacher(BaseModel):

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    EMPLOYMENT_TYPE_CHOICES = [
        ('full_time', 'Full-Time'),
        ('part_time', 'Part-Time'),
        ('contract', 'Contract'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    profile_photo = models.ImageField(upload_to='teachers/photos/', blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers')
    qualification = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    join_date = models.DateField()
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name} {self.last_name}")
        super().save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('teachers:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def get_update_url(self):
        return reverse('teachers:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('teachers:delete', args=[self.pk])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

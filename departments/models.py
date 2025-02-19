from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from config.utils import BaseModel
from django.conf import settings


class Department(BaseModel):
    STATUS_CHOICES = [
        ('active', 'active'),
        ('inactive', 'inactive'),
    ]

    HEAD_CHOICES = [
        ('OW', 'Olivia Williams'),
        ('EJ', 'Ethan Johnson'),
        ('BC', 'Benjamin Carter'),
        ('SM', 'Sophia Martinez'),
        ('DA', 'Daniel Anderson'),
    ]

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    head_of_department = models.CharField(max_length=2, choices=HEAD_CHOICES)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.EmailField(unique=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('departments:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def get_update_url(self):
        return reverse('departments:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('departments:delete', args=[self.pk])

    def __str__(self):
        return self.name

from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from teachers.models import Teacher
from config.utils import BaseModel
from django.conf import settings

class Group(BaseModel):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    GRADE_LEVEL_CHOICES = [
        ('grade_9', 'Grade 9'),
        ('grade_10', 'Grade 10'),
        ('grade_11', 'Grade 11'),
        ('grade_12', 'Grade 12'),
    ]

    SCHEDULE_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    ]

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    grade_level = models.CharField(max_length=20, choices=GRADE_LEVEL_CHOICES)
    schedule = models.CharField(max_length=20, choices=SCHEDULE_CHOICES)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='groups')
    academic_year = models.CharField(max_length=10)
    max_students = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('groups:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def get_update_url(self):
        return reverse('groups:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('groups:delete', args=[self.pk])

    def __str__(self):
        return f"{self.name} - {self.get_grade_level_display()}"

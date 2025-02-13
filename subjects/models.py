from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
from config.utils import BaseModel
from teachers.models import Teacher
from departments.models import Department

class Subject(BaseModel):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    GRADE_LEVEL_CHOICES = [
        ('grade_1', 'Grade 1'),
        ('grade_2', 'Grade 2'),
        ('grade_3', 'Grade 3'),
        ('grade_4', 'Grade 4'),
        ('grade_5', 'Grade 5'),
        ('grade_6', 'Grade 6'),
        ('grade_7', 'Grade 7'),
        ('grade_8', 'Grade 8'),
        ('grade_9', 'Grade 9'),
        ('grade_10', 'Grade 10'),
        ('grade_11', 'Grade 11'),
        ('grade_12', 'Grade 12'),
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subjects')
    description = models.TextField(blank=True, null=True)
    credit_hours = models.PositiveIntegerField()
    grade_level = models.CharField(max_length=10, choices=GRADE_LEVEL_CHOICES)
    prerequisites = models.TextField(blank=True, null=True)
    teachers = models.ManyToManyField(Teacher, related_name='subjects')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('subjects:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def get_update_url(self):
        return reverse('subjects:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('subjects:delete', args=[self.pk])

    def __str__(self):
        return self.name

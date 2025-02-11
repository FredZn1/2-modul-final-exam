from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from config.utils import BaseModel
from teachers.models import Teacher
from subjects.models import Subject


class Group(BaseModel):
    GRADE_LEVEL_CHOICES = [
        ('1', '1st Grade'),
        ('2', '2nd Grade'),
        ('3', '3rd Grade'),
        ('4', '4th Grade'),
        ('5', '5th Grade'),
        ('6', '6th Grade'),
        ('7', '7th Grade'),
        ('8', '8th Grade'),
        ('9', '9th Grade'),
        ('10', '10th Grade'),
        ('11', '11th Grade'),
        ('12', '12th Grade'),
    ]

    STATUS_CHOICES = [
        ('a', 'Active'),
        ('i', 'Inactive'),
        ('c', 'Closed'),
    ]

    SCHEDULE_CHOICES = [
        ('in', 'In the morning'),
        ('af', 'Afternoon'),
        ('ev', 'Evening'),
        ('we', 'Weekend'),
    ]

    group_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    academic_year = models.CharField(max_length=9)
    grade_level = models.CharField(max_length=2, choices=GRADE_LEVEL_CHOICES)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='a')
    schedule = models.CharField(max_length=2, choices=SCHEDULE_CHOICES, default='in')
    max_students = models.PositiveIntegerField(default=30)
    description = models.TextField(blank=True, null=True)
    subjects = models.ManyToManyField(Subject, related_name='groups', blank=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name='groups', null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.group_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:detail', args=[self.pk, self.slug])

    def get_update_url(self):
        return reverse('groups:update', args=[self.pk, self.slug])

    def get_delete_url(self):
        return reverse('groups:delete', args=[self.pk, self.slug])

    def __str__(self):
        return f"{self.group_name} ({self.get_grade_level_display()}) - {self.get_schedule_display()}"

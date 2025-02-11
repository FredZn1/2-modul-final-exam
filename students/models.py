from django.db import models
from django.shortcuts import reverse
from config.utils import BaseModel
from groups.models import Group


class Student(BaseModel):
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
        ('C', 'Closed'),
    ]

    SELECT_GENDER = [
        ('mal', 'Male'),
        ('fem', 'Female'),
    ]

    GRADE_CHOICES = [
        ('1', 'Grade 1'),
        ('2', 'Grade 2'),
        ('3', 'Grade 3'),
        ('4', 'Grade 4'),
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
        ('7', 'Grade 7'),
        ('8', 'Grade 8'),
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
        ('11', 'Grade 11'),
        ('12', 'Grade 12'),
    ]

    image = models.ImageField(upload_to='students_images/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        related_name='student_members',
        null=True, blank=True
    )
    date_of_birth = models.DateField()
    telephone_number = models.CharField(max_length=13)
    address = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    gender = models.CharField(max_length=3, choices=SELECT_GENDER)
    parent_name = models.CharField(max_length=100)
    parent_phone_number = models.CharField(max_length=13)
    parent_email = models.EmailField(unique=True)

    def get_detail_url(self):
        return reverse('students:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('students:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('students:delete', args=[self.pk])

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_status_display()})"

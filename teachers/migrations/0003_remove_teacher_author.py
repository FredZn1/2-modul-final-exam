# Generated by Django 5.1.6 on 2025-02-12 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_teacher_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='author',
        ),
    ]

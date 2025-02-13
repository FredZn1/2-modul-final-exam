# Generated by Django 5.1.6 on 2025-02-11 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('head_of_department', models.CharField(choices=[('OW', 'Olivia Williams'), ('EJ', 'Ethan Johnson'), ('BC', 'Benjamin Carter'), ('SM', 'Sophia Martinez'), ('DA', 'Daniel Anderson')], max_length=2)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_email', models.EmailField(max_length=254, unique=True)),
                ('contact_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

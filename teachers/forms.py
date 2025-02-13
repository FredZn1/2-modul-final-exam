from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name', 'last_name', 'profile_photo', 'email', 'phone_number',
            'department', 'qualification', 'address', 'join_date',
            'employment_type', 'status'
        ]

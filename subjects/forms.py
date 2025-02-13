from django import forms
from .models import Subject

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = [
            'name', 'department', 'description', 'credit_hours', 'grade_level',
            'prerequisites', 'teachers', 'status'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter subject name',
            }),
            'department': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter subject description',
                'rows': 4,
            }),
            'credit_hours': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter credit hours',
            }),
            'grade_level': forms.Select(choices=Subject.GRADE_LEVEL_CHOICES, attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'prerequisites': forms.SelectMultiple(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'teachers': forms.SelectMultiple(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Subject.objects.filter(name=name).exists():
            raise forms.ValidationError("A subject with this name already exists.")
        return name

    def clean_credit_hours(self):
        credit_hours = self.cleaned_data.get('credit_hours')
        if credit_hours <= 0:
            raise forms.ValidationError("Credit hours must be greater than zero.")
        return credit_hours

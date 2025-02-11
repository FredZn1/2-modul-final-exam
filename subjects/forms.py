from django import forms
from .models import Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fan nomi'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'credit_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'grade_level': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_credit_hours(self):
        credit_hours = self.cleaned_data.get('credit_hours')
        if credit_hours < 1:
            raise forms.ValidationError("Kredit soati 1 dan kam bo‘lmasligi kerak!")
        return credit_hours

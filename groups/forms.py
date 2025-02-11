from django import forms
from .models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

        widgets = {
            'group_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Guruh nomi'}),
            'academic_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'grade_level': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'schedule': forms.Select(attrs={'class': 'form-select'}),
            'subjects': forms.SelectMultiple(attrs={'class': 'form-select'}),  # Ko‘plik bo‘lsa
            'teacher': forms.Select(attrs={'class': 'form-select'}),
            'max_students': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Avtomatik yoki qo‘lda kiriting'}),
        }

    def clean_academic_year(self):
        academic_year = self.cleaned_data.get('academic_year')
        if academic_year < 1 or academic_year > 1000:
            raise forms.ValidationError("Akademik yil 2000-2100 oralig‘ida bo‘lishi kerak!")
        return academic_year

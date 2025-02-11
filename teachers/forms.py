from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ism'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiya'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Manzilni kiriting'}),
            'join_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'yyyy-mm-dd'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'employment_type': forms.Select(attrs={'class': 'form-select'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),  # ForeignKey uchun SelectMultiple emas!
        }

    def clean_join_date(self):
        join_date = self.cleaned_data.get('join_date')
        if not join_date:
            raise forms.ValidationError("Iltimos, ishga kirish sanasini kiriting!")
        return join_date

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name', '').strip()
        if not first_name:
            raise forms.ValidationError("Iltimos, ismni kiriting!")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name', '').strip()
        if not last_name:
            raise forms.ValidationError("Iltimos, familiyani kiriting!")
        return last_name

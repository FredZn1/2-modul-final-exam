from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ism'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiya'}),
            'group': forms.Select(attrs={'class': 'form-select'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'telephone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'grade': forms.Select(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'parent_name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_telephone_number(self):
        phone = self.cleaned_data.get('telephone_number')
        if not phone.isdigit():
            raise forms.ValidationError("Telefon raqam faqat raqamlardan iborat bo‘lishi kerak!")
        return phone

    def clean_parent_phone_number(self):
        phone = self.cleaned_data.get('parent_phone_number')
        if not phone.isdigit():
            raise forms.ValidationError("Ota-ona telefon raqami faqat raqamlardan iborat bo‘lishi kerak!")
        return phone

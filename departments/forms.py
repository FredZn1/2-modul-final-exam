from django import forms
from .models import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'head_of_department', 'descriptions', 'location', 'contact_email', 'phone_number']

        widgets = {
            'department_name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Bo‘lim nomi'}),
            'head_of_department': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'descriptions': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'rows': 3, 'placeholder': 'Bo‘lim haqida'}),
            'location': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Manzil'}),
            'contact_email': forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Telefon'}),
        }

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.isdigit():
            raise forms.ValidationError("Telefon raqami faqat raqamlardan iborat bo‘lishi kerak!")
        if not (7 <= len(phone) <= 15):
            raise forms.ValidationError("Telefon raqami 7-15 ta belgidan iborat bo‘lishi kerak!")
        return phone

    def clean_contact_email(self):
        email = self.cleaned_data.get('contact_email')
        if not email:
            raise forms.ValidationError("Email maydoni bo‘sh bo‘lishi mumkin emas!")
        return email

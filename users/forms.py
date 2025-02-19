from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password
from .models import CustomUser, UserProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_custom_styles()

    def apply_custom_styles(self):
        field_classes = {
            'email': 'block w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500',
            'username': 'block w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500',
            'first_name': 'block w-full px-3 py-2 border rounded-lg',
            'last_name': 'block w-full px-3 py-2 border rounded-lg',
        }
        for field_name, css_class in field_classes.items():
            self.fields[field_name].widget.attrs.update({'class': css_class})


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_custom_styles()

    def apply_custom_styles(self):
        field_classes = {
            'username': 'block w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500',
            'password': 'block w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500',
        }
        for field_name, css_class in field_classes.items():
            self.fields[field_name].widget.attrs.update({'class': css_class})


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
    )

    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-3 py-2 border rounded-md'}),
    )

    new_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
        label="New Password",
    )

    repeat_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
        label="Repeat Password",
    )

    class Meta:
        model = UserProfile
        fields = ('bio', 'birth_date', 'phone_number', 'image')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['username'].initial = user.username

        for field in self.fields:
            if field not in ["birth_date", "new_password", "repeat_password"]:
                self.fields[field].widget.attrs.update({'class': 'w-full px-3 py-2 border rounded-md'})

        self.fields['bio'].widget.attrs.update({'rows': '4'})

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        repeat_password = cleaned_data.get("repeat_password")

        if new_password or repeat_password:
            if new_password != repeat_password:
                raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user_profile = super().save(commit=False)
        new_password = self.cleaned_data.get("new_password")

        if new_password:
            user_profile.user.password = make_password(new_password)
            user_profile.user.save()

        username = self.cleaned_data.get("username")
        if username:
            user_profile.user.username = username
            user_profile.user.save()

        if commit:
            user_profile.save()

        return user_profile

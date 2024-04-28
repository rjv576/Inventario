from django import forms
from django.core import validators

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name', 'is_staff', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if len(password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

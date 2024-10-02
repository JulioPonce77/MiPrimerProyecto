from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserAuthentication

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserAuthentication
        fields = ('email',)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Correo electrónico',
        'id': 'email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contraseña',
        'id': 'password1'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirma tu contraseña',
        'id': 'password2'
    }))

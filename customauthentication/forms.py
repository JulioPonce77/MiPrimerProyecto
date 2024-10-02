from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserAuthentication  # Importa el modelo aquí

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text='Requerido. Ingrese un correo electrónico válido.'
    )

    class Meta:
        model = CustomUserAuthentication
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

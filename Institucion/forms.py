#FormsModels----------------
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

#BBDD----------------
from .models import SystemUser


class UserRegisterForm_PA(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = SystemUser
        fields = ['username', 'email', 'password1', 'password2', 'is_PA', 'is_PD',]
        help_texts = {k: "" for k in fields}

class UserRegisterForm_PD(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = SystemUser
        fields = ['username', 'email', 'password1', 'password2', 'is_PA', 'is_PD',]
        help_texts = {k: "" for k in fields}
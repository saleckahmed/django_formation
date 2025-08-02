from django import forms
from .models import Utilisateur

class LoginForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }),
            'password': forms.PasswordInput(attrs={  # Better to use PasswordInput
                'class': 'form-control',
                'placeholder': 'Enter password'
            })
        }

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'password', 'role', 'telephone']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }),
            'password': forms.PasswordInput(attrs={ 
                'class': 'form-control',
                'placeholder': 'Enter password'
            }),
            'role': forms.Select(attrs={
                'class': 'form-control',
                
            }),
            'telephone': forms.TextInput(attrs={ 
                'class': 'form-control',
                'placeholder': 'Enter phone'
            }),
        } 
        
        error_messages = {
            'username': {
                'required': "Username is required.",
            },
            'role': {
                'required': "Role is required.",
            },
            'password': {
                'required': "Password is required.",
            }
        }

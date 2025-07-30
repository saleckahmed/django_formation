from django import forms
from .models import Annonce, Category

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ['titre', 'description', 'prix', 'statut', 'image']  
        
        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'px-2 py-1 rounded',
                'placeholder': 'Titre'
            }),
            
            'description': forms.Textarea(attrs={ 
                'class': 'px-2 py-1 rounded',
                'placeholder': 'Description',
                'rows': 4 
            }),
            
            'prix': forms.NumberInput(attrs={ 
                'class': 'px-2 py-1 rounded',
                'placeholder': 'Prix',
                'step': '0.01'  
            }),
            
            'statut': forms.Select(attrs={ 
                'class': 'px-2 py-1 rounded'
            }),
            
            'image': forms.ClearableFileInput(attrs={  
                'class': 'px-2 py-1 rounded',
            })
        }
        error_messages = {
            'titre': {
                'required': "titre  is required",
            }, 
            'description': {
                'required': "description is required",
            },
            'prix': {
                'required': "prix is required",
            },
            'statut': {
                'required': "statut is required",
            },
            'image': {
                'required': "imageis required",
            }
        }

class CategoryForm(forms.ModelForm):
    class Meta: 
        model = Category
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs = {
                'class': 'px-2 py-1 rounded ',
                'placeholder': 'entre un category'
            })
        }

        error_messages = {
            'name': {
                'required': "Category name is required",
            }
        }
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
            'required': "Title is required.",
            'max_length': "Title is too long.",
        },
        'description': {
            'required': "Description is required.",
        },
        'prix': {
            'required': "Price is required.",
            'invalid': "Enter a valid price.",
            'min_value': "Price must be greater than 0.",
        },
        'statut': {
            'required': "Status is required.",
            'invalid_choice': "Select a valid status.",
        },
        'image': {
            'required': "Image is required.",
            'invalid': "Upload a valid image file.",
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
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """this class is a form for creating and updating a product"""

    class Meta:
        model = Product
        fields = ["name", "description", "category", "price", "quantity", "image"]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Recipe title...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write recipe contents...'
            }),
            'category': forms.Select(attrs={
                'class': 'custom-select'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control btn btn-primary',
                'id': "customFile"
            })
        }

from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address','email', 'city']
        widgets = {
            'first_name' : forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'address' : forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'city' : forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            )
        }


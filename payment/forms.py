from django import forms

class MpesaForm(forms.Form):
    phone_number = forms.CharField(widget=forms.TextInput(
                                    attrs={"class":"form-control"}
    ))

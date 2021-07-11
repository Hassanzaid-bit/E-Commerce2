from django.db.models import fields
from .models import Computer, Review, Portable
from django import forms


class ImageForm(forms.ModelForm):
    class Meta:
        model = Portable
        fields = ['Brand', 'type', 'memory', 'image', 'price', 'screen_size', 'series', 'model']  

 

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name','body',)
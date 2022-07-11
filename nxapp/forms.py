from django import forms
from django.forms import ModelForm
from .models import Newsletter

class NewsLetterForm(ModelForm):
    
    email = forms.EmailField(max_length=30)

    class Meta:
        model = Newsletter
        fields = ['email']
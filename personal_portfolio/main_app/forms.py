# forms.py
from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    full_name = forms.CharField(
        max_length=70,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'fullName',
            'placeholder': 'Enter your full name'
        })
    )
    email = forms.EmailField(
        validators=[EmailValidator()],
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'emailAddress',
            'placeholder': 'Enter your email'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'message',
            'placeholder': 'Write your message here',
            'style': 'height: 10rem'
        })
    )

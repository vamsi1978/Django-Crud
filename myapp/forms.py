from dataclasses import fields
from django import forms
from .models import User,Content

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields="__all__"
class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields="__all__"

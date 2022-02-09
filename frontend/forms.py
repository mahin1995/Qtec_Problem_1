from dataclasses import fields
from django import forms
from api.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    mobile = forms.CharField(max_length=15, min_length=10)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'mobile' ]
        

class KeyWordForm(forms.ModelForm):
    describe = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    class Meta:
        model=keyword
        fields ='__all__'
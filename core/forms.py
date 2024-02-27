from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Логин"}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Пароль'}), label='')

    def clean_password(self):
        password = self.cleaned_data['password']
        username = self.cleaned_data['username']
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValidationError('Неверный email или пароль')
        else:
            if not(check_password(password, user.password)):
                raise ValidationError('Неверный email или пароль')
        return password
    
class ClientForm(forms.Form):
    name_point = forms.CharField()

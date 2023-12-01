from django import forms
import random

from django.shortcuts import render
from requests import request
class SearchPokemons(forms.Form):
    Search = forms.CharField(label='srth', max_length=100)
    print("Вы ввели значение: ")
from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from django.core.exceptions import ValidationError 
from django.forms.fields import EmailField 
from django.forms.forms import Form 
class CustomUserCreationForm(UserCreationForm): 
    username = forms.CharField(label='username', min_length=5, max_length=150) 
    email = forms.EmailField(label='email') 
    password1 = forms.CharField(label='password', widget=forms.PasswordInput) 
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput) 
 
    def username_clean(self): 
        username = self.cleaned_data['username'].lower() 
        new = User.objects.filter(username = username) 
        if new.count(): 
            raise ValidationError("Пользователь сущствует!") 
        return username 
 
    def email_clean(self): 
        email = self.cleaned_data['email']
        new = User.objects.filter(email=email) 
        if new.count(): 
            raise forms.ValidationError(" Email Already Exist") 
        return email 
 
    def clean_password2(self): 
        password1 = self.cleaned_data['password1'] 
        password2 = self.cleaned_data['password2'] 
 
        if password1 and password2 and password1 != password2: 
            raise ValidationError("Password don't match") 
        return password2 
 
    def save(self, commit = True): 
        random_code = random.randint(100000,1000000)
        new_user_email = self.cleaned_data["email"]
        user = User.objects.create_user( 
                    self.cleaned_data['username'], 
                    self.cleaned_data['email'], 
                    self.cleaned_data['password1'] 
                ) 
        return user 
        # if User.objects.filter(email=new_user_email).exists():
        #     raise forms.ValidationError("Email is not unique")
        # else:
            
        #     user = User.objects.create_user( 
        #             self.cleaned_data['username'], 
        #             self.cleaned_data['email'], 
        #             self.cleaned_data['password1'] 
        #         ) 
        #     return user 

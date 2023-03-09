from dataclasses import fields

from django.forms import ImageField, ModelForm, TextInput, EmailInput, IntegerField

from django import forms
from flask import request
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Signupform(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'password1','password2')

class Messageform(ModelForm):
    class meta:
        model = Message
        fields = "__all__"
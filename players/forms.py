# -*- coding: utf-8 -*-

from players.models import player
from django.contrib.auth.models import User
from django import forms

class PlayerForm(forms.ModelForm):
   #username = forms.CharField(label='Užívateľské meno', widget=forms.TextInput, required=True)
    password1 = forms.CharField(label='Heslo', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Heslo znovu', widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(label='Meno', widget=forms.TextInput, required=False)
    last_name = forms.CharField(label='Priezvisko', widget=forms.TextInput, required=False)
    city = forms.CharField(label='Mesto', widget=forms.TextInput, required=False)
    street = forms.CharField(label='Ulica', widget=forms.TextInput, required=False)
    email = forms.CharField(label='Email', widget=forms.TextInput, required=True)
    phone = forms.DecimalField(label='Mobil',widget=forms.TextInput, required=False)
    photo = forms.FileField(label='Profilová fotka',widget=forms.FileInput, required=False)


    class Meta:
        model = player
        model = User
        exclude = ('last_login','is_superuser', 'is_staff', 'is_active','date_joined','username','password','groups','user_permissions')

    def clean_password2(self):
        if self.cleaned_data.get('password1') != self.cleaned_data['password2']:
            raise forms.ValidationError('Zadané heslá sú odlišné !')

        return self.cleaned_data['password2']
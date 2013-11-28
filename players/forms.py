# -*- coding: utf-8 -*-
from django.forms.extras.widgets import SelectDateWidget
from players.models import player
from django import forms

class PlayerForm(forms.ModelForm):
    #username = forms.CharField(label='Užívateľské meno', widget=forms.CharField(), required=True)
    #password1 = forms.CharField(label='Heslo', widget=forms.PasswordInput, required=True)
    #password2 = forms.CharField(label='Heslo znovu', widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(label='Meno', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Meno'}), required=False)
    last_name = forms.CharField(label='Priezvisko', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Priezvisko'}), required=False)
    gender = forms.CharField(label='Pohlavie',widget=forms.Select(choices = player.GENDER_CHOICES, attrs={'id': 'select', 'class': 'form-control'}), required=True )
    date_of_birth = forms.CharField(label='Dátum nar.',widget=forms.TextInput(attrs={'id': 'datepicker', 'class': 'form-control','type':'text','uniq':'calendar'}), required=True )
    countryPart = forms.CharField(label='Kraj',widget=forms.Select(choices = player.KRAJE_CHOICES, attrs={'id': 'select', 'class': 'form-control'}), required=True )
    city = forms.CharField(label='Mesto', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Mesto'}), required=False)
    street = forms.CharField(label='Ulica', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Ulica'}), required=False)
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Email'}), required=True)
    phone = forms.DecimalField(label='Mobil',widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Telefón'}), required=False)
    about_me = forms.CharField(label='O mne',widget=forms.Textarea(attrs={'id': 'textArea', 'class': 'form-control','rows':'3','type':'text','placeholder':'Napíš nám niečo o sebe'}), required=False)
    #photo = forms.FileField(label='Profilová fotka',widget=forms.FileInput, required=False)


    class Meta:
        model = player
        fields = ('first_name','last_name','gender','date_of_birth','countryPart','city', 'street','email','phone','about_me')

    def clean_password2(self):
        if self.cleaned_data.get('password1') != self.cleaned_data['password2']:
            raise forms.ValidationError('Zadané heslá sú odlišné !')

        return self.cleaned_data['password2']
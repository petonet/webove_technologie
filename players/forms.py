# -*- coding: utf-8 -*-
from django.forms.extras.widgets import SelectDateWidget
from players.models import player
from django.contrib.auth.models import User
from django import forms
import re,views,imghdr
from HrajAirsoft import settings

class PlayerForm(forms.ModelForm):

    first_name = forms.CharField(label='Meno', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Meno'}), required=False)
    last_name = forms.CharField(label='Priezvisko', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Priezvisko'}), required=False)
    gender = forms.CharField(label='Pohlavie',widget=forms.Select(choices = player.GENDER_CHOICES, attrs={'id': 'select', 'class': 'form-control'}), required=True )
    date_of_birth = forms.CharField(label='Dátum nar. *',widget=forms.TextInput(attrs={'id': 'datepicker', 'class': 'form-control','type':'text','uniq':'calendar'}), required=False )
    countryPart = forms.CharField(label='Kraj',widget=forms.Select(choices = player.KRAJE_CHOICES, attrs={'id': 'select', 'class': 'form-control'}), required=True )
    city = forms.CharField(label='Mesto', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Mesto'}), required=False)
    street = forms.CharField(label='Adresa', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Ulica'}), required=False)
    email = forms.CharField(label='Email  *', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Email'}), required=False)
    phone = forms.CharField(label='Mobil',widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Telefón'}), required=False)
    about_me = forms.CharField(label='O mne',widget=forms.Textarea(attrs={'id': 'textArea', 'class': 'form-control','rows':'3','type':'text','placeholder':'Napíš nám niečo o sebe'}), required=False)


    class Meta:
        model = player
        fields = ('first_name','last_name','gender','date_of_birth','countryPart','city', 'street','email','phone','about_me')


    def clean_email(self):
        emailPattern = "^([\\w\\-\\.]+)@((\\[([0-9]{1,3}\\.){3}[0-9]{1,3}\\])|(([\\w\\-]+\\.)+)([a-zA-Z]{2,4}))$"
        email = self.cleaned_data['email']
        if len(email) == 0:
            raise forms.ValidationError("Pole je prázdne !")
        if re.match(emailPattern,email) is None:
            raise forms.ValidationError("Nesprávny formát - príklad: jozko@tuke.sk !")
        return email

    def clean_phone(self):
        phoneNumberPattern = "^[ ]*[(]?([+]|[0-9])?[ ]*[0-9]+[ ]*[)]?[ ]*[/]?[ |0-9]+$"
        phone = self.cleaned_data['phone']
        if re.match(phoneNumberPattern,phone) is None and len(phone) != 0 :
            raise forms.ValidationError("Nesprávny formát - príklad: +421 944 511 alebo 051 / 77 456 12 alebo 0908 123 456 !")
        return phone


    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if len(date_of_birth) == 0:
            raise forms.ValidationError("Pole je prázdne !")
        if views.validateDate(date_of_birth) != True:
            raise forms.ValidationError("Nesprávny formát - musí byť v tvare rok-mesiac-deň ! príklad: 1990-12-22")
        return date_of_birth

class RegistrationForm(forms.Form):

    username = forms.CharField(label='Login *', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Používateľské meno'}), required=False)
    password1 = forms.CharField(label='Heslo *', widget=forms.PasswordInput(attrs={'id': 'inputPassword', 'class': 'form-control','type':'password','placeholder':'Heslo'}), required=False)
    password2 = forms.CharField(label='Heslo znovu *', widget=forms.PasswordInput(attrs={'id': 'inputPassword', 'class': 'form-control','type':'password','placeholder':'Heslo znovu'}), required=False)

    first_name = forms.CharField(label='Meno', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Meno'}), required=False)
    last_name = forms.CharField(label='Priezvisko', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Priezvisko'}), required=False)

    email = forms.CharField(label='Email *', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Email'}), required=False)
    gender = forms.CharField(label='Pohlavie',widget=forms.Select(choices = player.GENDER_CHOICES, attrs={'id': 'select', 'class': 'form-control'}), required=True )
    date_of_birth = forms.CharField(label='Dátum nar. *',widget=forms.TextInput(attrs={'id': 'datepicker', 'class': 'form-control','type':'text','uniq':'calendar'}), required=False )

    countryPart = forms.CharField(label='Kraj',widget=forms.Select(choices = player.KRAJE_CHOICES, attrs={'id': 'select', 'class': 'form-control'}), required=True )
    city = forms.CharField(label='Mesto', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Mesto'}), required=False)
    street = forms.CharField(label='Adresa', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Ulica'}), required=False)


    phone = forms.CharField(label='Mobil',widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Telefón'}), required=False)
    photo = forms.FileField(label='Profil. fotka',widget=forms.FileInput(attrs={'id': 'inputEmail', 'class': 'form-control','placeholder':'Path to file'}), required=False)

    about_me = forms.CharField(label='O mne',widget=forms.Textarea(attrs={'id': 'textArea', 'class': 'form-control','rows':'3','type':'text','placeholder':'Napíš nám niečo o sebe'}), required=False)

    def clean_username(self):
        data = self.cleaned_data['username']
        if len(data) == 0:
            raise forms.ValidationError("Login je prázdny !")
        if len(User.objects.filter(username=data)) != 0:
            raise forms.ValidationError("Toto používateľské meno už existuje !")
        return data

    def clean_password2(self):
        if self.cleaned_data.get('password1') != self.cleaned_data['password2']:
            raise forms.ValidationError('Zadané heslá sú odlišné !')
        if len(self.cleaned_data.get('password1')) == 0 or len(self.cleaned_data.get('password1')) == 0:
            raise forms.ValidationError('Chýba heslo v poli Heslo alebo Heslo znovu !')
        if len(self.cleaned_data.get('password1')) == 0 and len(self.cleaned_data.get('password1')) == 0:
            raise forms.ValidationError('Chýba heslo v poli Heslo a Heslo znovu !')
        return self.cleaned_data['password2']

    def clean_email(self):
        emailPattern = "^([\\w\\-\\.]+)@((\\[([0-9]{1,3}\\.){3}[0-9]{1,3}\\])|(([\\w\\-]+\\.)+)([a-zA-Z]{2,4}))$"
        email = self.cleaned_data['email']
        if len(email) == 0:
            raise forms.ValidationError("Pole je prázdne !")
        if re.match(emailPattern,email) is None:
            raise forms.ValidationError("Nesprávny formát - príklad: jozko@tuke.sk !")
        return email

    def clean_phone(self):
        phoneNumberPattern = "^[ ]*[(]?([+]|[0-9])?[ ]*[0-9]+[ ]*[)]?[ ]*[/]?[ |0-9]+$"
        phone = self.cleaned_data['phone']
        if re.match(phoneNumberPattern,phone) is None and len(phone) != 0 :
            raise forms.ValidationError("Nesprávny formát - príklad: +421 944 511 alebo 051 / 77 456 12 alebo 0908 123 456 !")
        return phone


    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if len(date_of_birth) == 0:
            raise forms.ValidationError("Pole je prázdne !")
        if views.validateDate(date_of_birth) != True:
            raise forms.ValidationError("Nesprávny formát - musí byť v tvare rok-mesiac-deň ! príklad: 1990-12-22")
        return date_of_birth

    def clean_photo(self):
        photo = self.cleaned_data['photo']
        if photo is not None:
            if len(photo) != 0 and not imghdr.what(photo) :
                raise forms.ValidationError("Nie je to obrázok !")
        return photo

class ChangePassForm(forms.Form):

    old_password = forms.CharField(label='Aktuálne heslo *', widget=forms.PasswordInput(attrs={'id': 'inputPassword', 'class': 'form-control','type':'password','placeholder':'Aktuálne heslo'}), required=False)
    password1 = forms.CharField(label='Nové heslo *', widget=forms.PasswordInput(attrs={'id': 'inputPassword', 'class': 'form-control','type':'password','placeholder':'Nové heslo'}), required=False)
    password2 = forms.CharField(label='Nové heslo znovu *', widget=forms.PasswordInput(attrs={'id': 'inputPassword', 'class': 'form-control','type':'password','placeholder':'Nové heslo znovu'}), required=False)

    def clean_old_password(self):
        if len(self.cleaned_data.get('old_password')) == 0:
            raise forms.ValidationError('Povinné pole !')
        return self.cleaned_data['old_password']



    def clean_password1(self):
        if len(self.cleaned_data.get('password1')) == 0:
            raise forms.ValidationError('Povinné pole !')
        return self.cleaned_data['password1']


    def clean_password2(self):
        if len(self.cleaned_data.get('password2')) == 0:
            raise forms.ValidationError('Povinné pole !')
        if self.cleaned_data.get('password1') != self.cleaned_data['password2']:
            raise forms.ValidationError('Zadané heslá sú odlišné !')
        return self.cleaned_data['password2']
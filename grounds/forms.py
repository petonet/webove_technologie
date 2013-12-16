# -*- coding: utf-8 -*-

from players.models import player
from django.contrib.auth.models import User
from django import forms
from models import ground
from pilkit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

class AddGroundForm(forms.ModelForm):
   #username = forms.CharField(label='Užívateľské meno', widget=forms.TextInput, required=True)
    name = forms.CharField(label='Meno ihriska', widget=forms.TextInput(attrs={'class':'form-control form-control2'}), required=True, max_length=200,)
    #city = forms.CharField(label='Mesto', widget=forms.TextInput, required=True, max_length= 100)
   # street = forms.CharField(label='Ulica', widget=forms.TextInput, required=True)
    description = forms.CharField(label='Popis', widget=forms.Textarea, required=False)
    rate = forms.DecimalField(label='Hodnotenie', widget=forms.HiddenInput, required=False,initial=2.5)
    official = forms.BooleanField(label='Oficiálne ihrisko', widget=forms.CheckboxInput, required=False)
    pubDate = forms.CharField(label='Datum pridania', widget=forms.HiddenInput, required=False)
    photo = forms.ImageField(label='Fotka ihriska',widget=forms.FileInput, required=False,)
    user = forms.DecimalField(label='Pouzivatel', widget=forms.HiddenInput, required=False)
    Latitude=forms.DecimalField(widget=forms.HiddenInput,required=False)
    Longitude=forms.DecimalField(widget=forms.HiddenInput,required=False)


    class Meta:
        model = ground
        #model = User
        exclude = ('pubDate','user','rate','city','street')
        fields = ('name','city','street','description','official','photo')


# -*- coding: utf-8 -*-
from django import forms
from models import Event


class NewForm(forms.ModelForm):
    title = forms.CharField(label='Názov', widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Názov akcie'}), required=True)
    startOfActionDate = forms.CharField(label='Začiatok akcie', widget=forms.TextInput(attrs={'id': 'startDatepicker', 'placeholder': 'Dátum začiatku'}), required=True)
    startOfActionTime = forms.CharField(widget=forms.TextInput(attrs={'id': 'startTimePicker','placeholder': 'Čas'}), required=True)
    numberOfPlayers = forms.CharField(label='Počet účastníkov', widget=forms.TextInput(attrs={'placeholder': '0'}), required=True)
    login_sinceDate = forms.CharField(label='Prihlásenie povolené od', widget=forms.TextInput(attrs={'id':'loginDatepicker', 'placeholder': 'Dátum'}), required=True)
    login_sinceTime = forms.CharField(widget=forms.TextInput(attrs={'id': 'loginTimePicker','placeholder': 'Čas'}), required=True)
    prologue = forms.CharField(label='Prológ', widget=forms.Textarea(attrs={'type': 'text', 'placeholder': 'Prológ', 'cols': '75', 'rows': '5'}), required=False)
    scenario = forms.CharField(label='Scenár', widget=forms.Textarea(attrs={'type': 'text', 'placeholder': 'Scenár', 'cols': '75', 'rows': '5'}), required=True)
    organizationNotes = forms.CharField(label='Organizačné pokyny', widget=forms.Textarea(attrs={'type': 'text', 'placeholder': 'Organizačné pokyny', 'cols': '75', 'rows': '5'}), required=True)
    duration = forms.CharField(label='Trvanie', widget=forms.TextInput(attrs={'placeholder': '0'}), required=True)
    entryFee = forms.CharField(label='Vstupné', widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Vstupné'}), required=True)


    class Meta:
        model = Event
        fields = ('title','startOfActionDate', 'startOfActionTime','duration','login_sinceDate', 'login_sinceTime',
                  'numberOfPlayers','entryFee','prologue','scenario','organizationNotes','ground')
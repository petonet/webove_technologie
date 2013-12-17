# -*- coding: utf-8 -*-
from django.forms.extras.widgets import SelectDateWidget
from players.models import player
from django.contrib.auth.models import User
from models import Team
from django import forms
import re,views,imghdr
from HrajAirsoft import settings
from pilkit.processors import ResizeToFill
from imagekit.forms import ProcessedImageField

class addTeamForm(forms.Form):
    name = forms.CharField(label='Názov tímu *', widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'form-control','type':'text','placeholder':'Napíš názov tohto tímu'}), required=False)
    description = forms.CharField(label='Popis tímu',widget=forms.Textarea(attrs={'id': 'textArea', 'class': 'form-control','rows':'3','type':'text','placeholder':'Napíš niečo o tomto tíme alebo nechaj zatiaľ prázdne'}), required=False)
    team_logo = forms.FileField(label='Logo tímu',widget=forms.FileInput(attrs={'id': 'inputEmail', 'class': 'form-control','placeholder':'Path to file'}), required=False)
    big_logo = forms.FileField(label='Logo tímovej stránky',widget=forms.FileInput(attrs={'id': 'inputEmail', 'class': 'form-control','placeholder':'Path to file'}), required=False)
    last_name = forms.CharField(label='nevidis',widget=forms.TextInput(attrs={'type':'hidden','id': 'hidden'}), required=False)
    def clean_name(self):
        data = self.cleaned_data['name']
        if len(data) == 0:
            raise forms.ValidationError("Musíš uviesť názov tímu !")
        print self.cleaned_data.get('last_name')
        print data
        if len(Team.objects.filter(name=data)) != 0 and self.data.get('last_name') != data :
            raise forms.ValidationError("Tím s týmto názvom už existuje !")
        return data

    def clean_team_logo(self):
        photo = self.cleaned_data['team_logo']
        if photo is not None:
            if len(photo) != 0 and not imghdr.what(photo) :
                raise forms.ValidationError("Nie je to obrázok !")
        return photo

    def clean_big_logo(self):
        photo = self.cleaned_data['big_logo']
        if photo is not None:
            if len(photo) != 0 and not imghdr.what(photo) :
                raise forms.ValidationError("Nie je to obrázok !")
        return photo



class deleteRequestToTeam(forms.Form):

    team_id = forms.CharField(label='nevidis',widget=forms.TextInput(attrs={'type':'hidden','id': 'hidden'}), required=False)

class addRequestToTeam(forms.Form):

    team_id = forms.CharField(label='nevidis',widget=forms.TextInput(attrs={'type':'hidden','id': 'hidden'}), required=False)

class deleteTeam(forms.Form):

    team_id = forms.CharField(label='nevidis',widget=forms.TextInput(attrs={'type':'hidden','id': 'hidden'}), required=False)

class addingPlayer(forms.Form):

    team_id = forms.CharField(label='team_id',widget=forms.TextInput(attrs={'type':'hidden','id': 'hidden'}), required=False)
    user_id = forms.CharField(label='user_id',widget=forms.TextInput(attrs={'type':'hidden','id': 'hidden'}), required=False)
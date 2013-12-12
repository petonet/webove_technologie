# -*- coding: utf-8 -*-
import datetime
import re
from django import forms
from models import Event
from grounds.models import ground
from django.core.exceptions import ValidationError


class NewForm(forms.ModelForm):
    title = forms.CharField(label='Názov', widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Názov akcie'}), required=False)
    startOfActionDate = forms.CharField(label='Začiatok akcie', widget=forms.TextInput(attrs={'id': 'startDatepicker', 'placeholder': 'Dátum začiatku'}), required=False)
    startOfActionTime = forms.CharField(widget=forms.TextInput(attrs={'id': 'startTimePicker','placeholder': 'Čas'}), required=False)
    numberOfPlayers = forms.IntegerField(label='Počet účastníkov', widget=forms.TextInput(attrs={'placeholder': '0'}), required=False)
    login_sinceDate = forms.CharField(label='Prihlásenie povolené od', widget=forms.TextInput(attrs={'id':'loginDatepicker', 'placeholder': 'Dátum'}), required=False)
    login_sinceTime = forms.CharField(widget=forms.TextInput(attrs={'id': 'loginTimePicker','placeholder': 'Čas'}), required=False)
    prologue = forms.CharField(label='Prológ', widget=forms.Textarea(attrs={'type': 'text', 'placeholder': 'Prológ', 'cols': '75', 'rows': '5'}), required=False)
    scenario = forms.CharField(label='Scenár', widget=forms.Textarea(attrs={'type': 'text', 'placeholder': 'Scenár', 'cols': '75', 'rows': '5'}), required=False)
    organizationNotes = forms.CharField(label='Organizačné pokyny', widget=forms.Textarea(attrs={'type': 'text', 'placeholder': 'Organizačné pokyny', 'cols': '75', 'rows': '5'}), required=False)
    duration = forms.CharField(label='Trvanie', widget=forms.TextInput(attrs={'placeholder': '0'}), required=False)
    entryFee = forms.CharField(label='Vstupné', widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Vstupné'}), required=False)
    ground = forms.ModelChoiceField(label='Miesto',queryset= ground.objects.all().order_by('name'), empty_label='Nové miesto', required=False)


    class Meta:
        model = Event
        fields = ('title','startOfActionDate', 'startOfActionTime','duration','login_sinceDate', 'login_sinceTime',
                  'numberOfPlayers','entryFee','prologue','scenario','organizationNotes','ground')

    def clean_numberOfPlayers(self):
        value = self.cleaned_data.get("numberOfPlayers")
        if value < 1:
            raise ValidationError(u'Počet účastníkov musí byť väčší ako 1')
        return value

    def clean_title(self):
        value = self.cleaned_data.get("title")
        if value == "":
            raise ValidationError(u'Nezadali ste názov akcie')
        return value

    def clean_login_sinceTime(self):
        startDate = self.cleaned_data.get("startOfActionDate")
        if startDate == "":
            raise ValidationError(u'Nezadali ste dátum začiatku akcie')
        startTime = self.cleaned_data.get("startOfActionTime")
        if startTime == "":
            raise ValidationError(u'Nezadali ste čas začiatku akcie')
        loginDate = self.cleaned_data.get("login_sinceDate")
        if loginDate == "":
            raise ValidationError(u'Nezadali ste dátum začiatku prihlasovania')
        loginTime = self.cleaned_data.get("login_sinceTime")
        if loginTime == "":
            raise ValidationError(u'Nezadali ste čas začiatku prihlasovania')
        if (self.checkDate(startDate) and self.checkDate(loginDate) and self.checkTime(startTime) and self.checkTime(loginTime)):
            splitStartDate = startDate.split(".")
            splitStartTime = startTime.split(":")
            splitLoginDate = loginDate.split(".")
            splitLoginTime = loginTime.split(":")
            startDateTime = datetime.datetime(int(float(splitStartDate[2])), int(float(splitStartDate[1])), int(float(splitStartDate[0])),
                                              int(float(splitStartTime[0])), int(float(splitStartTime[1])))
            loginDateTime = datetime.datetime(int(float(splitLoginDate[2])), int(float(splitLoginDate[1])), int(float(splitLoginDate[0])),
                                              int(float(splitLoginTime[0])), int(float(splitLoginTime[1])))
            difference = startDateTime - loginDateTime
            if difference.total_seconds() < 0:
                raise ValidationError(u'Začiatok prihlasovania musí byť pred začiatkom akcie')
        return loginTime

    def clean_duration(self):
        duration = self.cleaned_data.get("duration")
        if duration == "":
            raise ValidationError(u'Nezadali ste čas trvania akcie')
        self.checkTime(duration)
        return duration

    def clean_entryFee(self):
        fee = self.cleaned_data.get("entryFee")
        self.checkPrice(fee)
        return fee

    def clean_ground(self):
        latitude = self.cleaned_data.get("Latitude")
        longitude = self.cleaned_data.get("Longitude")
        if latitude == "" or longitude == "":
            raise ValidationError(u'Nevybrali ste miesto (Vybrané miesto je označené zeleným ukazovateľom)')

    def checkDate(self, date):
        pattern = "^\d{2}\.\d{2}\.\d{4}$"
        if (re.match(pattern, date) is None):
            raise ValidationError(u'Zlý formát dátumu')
            return False
        else:
            split = date.split(".")
            if int(float(split[0])) > 31:
                raise ValidationError(u'Zlý formát dátumu')
                return False
            if int(float(split[1])) > 12:
                raise ValidationError(u'Zlý formát dátumu')
                return False
        return True

    def checkTime(self, time):
        pattern = "^\d{1,2}\:\d{2}$"
        if (re.match(pattern, time) is None):
            raise ValidationError(u'Zlý formát času')
            return False
        else:
            split = time.split(":")
            if int(float(split[0])) < 0 or int(float(split[0])) > 23:
                raise ValidationError(u'Zlý formát času')
                return False
            if int(float(split[1])) > 59 or int(float(split[1])) < 0 :
                raise ValidationError(u'Zlý formát času')
                return False
        return True

    def checkPrice(self, price):
        pattern = "^(\d+\.\d+)|(\d+,\d+)|(\d+)$"
        if (re.match(pattern, price) is None):
            raise ValidationError(u'Nesprávny formát ceny')
            return False
        else:
            return True

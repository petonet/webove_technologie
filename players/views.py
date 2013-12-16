# -*- coding: utf-8 -*-

from django.views.decorators.csrf import csrf_exempt
from models import player
from forms import PlayerForm, RegistrationForm, ChangePassForm, ChangePhotoForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
#from players.views import profile
import datetime
from django.contrib.auth.models import User

def calculate_age(born):
    today = datetime.date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError: # narodenie 29.februara a aktualny rok nie je priestupny
        birthday = born.replace(year=today.year, day=born.day-1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year



def validateDate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return None

@login_required
def profile(request):

    try:
        profile = request.user.get_profile()
    except player.DoesNotExist:
        profile = player(user=request.user)

    saved = None

    if request.method == 'POST':
        form = PlayerForm(request.POST)

        if form.is_valid():

            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']

            request.user.email = form.cleaned_data['email']
            profile.gender = form.cleaned_data['gender']

            profile.date_of_birth = form.cleaned_data['date_of_birth']
            profile.countryPart = form.cleaned_data['countryPart']
            profile.city = form.cleaned_data['city']
            profile.street = form.cleaned_data['street']
            profile.email = form.cleaned_data['email']

            profile.phone = form.cleaned_data['phone']
            profile.about_me = form.cleaned_data['about_me']


            request.user.save()
            profile.save()
            saved = True

            return render_to_response('players/profile.html', {'form': form, 'saved': saved, }, context_instance=RequestContext(request))

        else:

            return render_to_response('players/profile.html', {'form': form, 'fail': True, }, context_instance=RequestContext(request))


    else:

        form = PlayerForm(initial={
                                   'username': request.user.username,
                                   'first_name': request.user.first_name,
                                   'last_name': request.user.last_name,
                                   'city': profile.city,
                                   'street': profile.street,
                                   'email': request.user.email,
                                   'phone': profile.phone,
                                   'gender': profile.gender,
                                   'date_of_birth': profile.date_of_birth,
                                   'about_me': profile.about_me,
                                   'countryPart': profile.countryPart,
        })


    return render_to_response('players/profile.html', { 'form': form }, context_instance=RequestContext(request))




def registration(request):

    emailPattern = "^([\\w\\-\\.]+)@((\\[([0-9]{1,3}\\.){3}[0-9]{1,3}\\])|(([\\w\\-]+\\.)+)([a-zA-Z]{2,4}))$"
    phoneNumberPattern = "^([+]|[0-9])?[/|[0-9]| ]+$"

    saved = None
    if request.method == 'POST':

        form = RegistrationForm(data=request.POST, files=request.FILES)

        if form.is_valid() and form.is_bound==True :

            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            email = form.cleaned_data['email']

            new_user = User.objects.create_user(username, email, password1)

            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']

            gender = form.cleaned_data['gender']
            date_of_birth = form.cleaned_data['date_of_birth']
            countryPart = form.cleaned_data['countryPart']
            city = form.cleaned_data['city']
            street = form.cleaned_data['street']
            phone = form.cleaned_data['phone']
            about_me = form.cleaned_data['about_me']
            photo = form.cleaned_data['photo']

            new_user.save()

            new_player = player(user=new_user,gender=gender,date_of_birth=date_of_birth,countryPart=countryPart,city=city,street=street,phone=phone,about_me=about_me,photo=photo,rank=0)
            new_player.save()

            saved = True

            return render_to_response('players/registration.html', {'form': form, 'saved': saved, 'reg':True }, context_instance=RequestContext(request))
        else:
            return render_to_response('players/registration.html', {'form': form, 'fail': True, 'reg':True }, context_instance=RequestContext(request))

    else:
        form = RegistrationForm({})
        return render_to_response('players/registration.html', {'form': form, 'reg':True }, context_instance=RequestContext(request))


@login_required
def changepass(request):

    saved = None
    if request.method == 'POST':

        form = ChangePassForm(request.POST)

        if form.is_valid() and form.is_bound==True :
            old_password = form.cleaned_data['old_password']
            password1 = form.cleaned_data['password1']
            if request.user.check_password(old_password):
                request.user.set_password(password1)
                request.user.save()
                return render_to_response('players/changepass.html', {'form': form, 'saved': True , 'changePass': True }, context_instance=RequestContext(request))
            else:
                return render_to_response('players/changepass.html', {'form': form, 'fail': True, 'changePass': True, 'badpassword': 'Zadal si nesprávne heslo !'}, context_instance=RequestContext(request))
        return render_to_response('players/changepass.html', {'form': form, 'fail': True, 'changePass': True }, context_instance=RequestContext(request))

    else:
        form = ChangePassForm({})
        return render_to_response('players/changepass.html', {'form': form, 'changePass': True }, context_instance=RequestContext(request))

@login_required
def aboutMe(request):
    try:
        info_about_player = request.user.get_profile()
    except player.DoesNotExist:
        info_about_player = player(user=request.user)

    age = calculate_age(info_about_player.date_of_birth)
    return render_to_response('players/aboutMe.html', {'info_about_player': info_about_player,'age':age }, context_instance=RequestContext(request))


@login_required
def changephoto(request):

    saved = None
    if request.method == 'POST':

        form = ChangePhotoForm(request.POST, files=request.FILES)

        if form.is_valid() and form.is_bound==True :
            photo = form.cleaned_data['photo']

            try:
                info_about_player = request.user.get_profile()
            except player.DoesNotExist:
                info_about_player = player(user=request.user)

            about_me = info_about_player.about_me
            city = info_about_player.city
            countryPart = info_about_player.countryPart
            date_of_birth = info_about_player.date_of_birth
            gender = info_about_player.gender
            phone = info_about_player.phone
            rank = info_about_player.rank
            street = info_about_player.street

            info_about_player.delete()

            new_player = player(user=request.user,gender=gender,date_of_birth=date_of_birth,countryPart=countryPart,city=city,street=street,phone=phone,about_me=about_me,photo=photo,rank=rank)

            new_player.save()

            return render_to_response('players/changephoto.html', {'form': form, 'saved': True , 'changePass': True, 'changephoto':True }, context_instance=RequestContext(request))
        else:
            return render_to_response('players/changephoto.html', {'form': form, 'fail': True, 'changePass': True, 'changephoto':True  }, context_instance=RequestContext(request))

    else:
        form = ChangePhotoForm({})
        return render_to_response('players/changephoto.html', {'form': form, 'changePass': True , 'changephoto':True }, context_instance=RequestContext(request))


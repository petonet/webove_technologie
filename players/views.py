from django.views.decorators.csrf import csrf_exempt
from models import player
from forms import PlayerForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
#from players.views import profile


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
            #'first_name','last_name','gender','date_of_birth','country_part','city', 'street','email','phone','about_me'
            #request.user.username = form.cleaned_data['username']
            #request.user.password1 = form.cleaned_data['password1']
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


            #if len(form.cleaned_data['password1']) > 0:
            #    request.user.set_password(form.cleaned_data['password1'])

            request.user.save()
            profile.save()
            saved = True
            return HttpResponseRedirect('/accounts/profile/saved/')
    else:
        #photo = player(user=request.user).photo

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
                                   'about_me' : profile.about_me,
                                   'countryPart': profile.countryPart,
        })


    return render_to_response('players/profile.html', {'form': form, 'saved': saved }, context_instance=RequestContext(request))
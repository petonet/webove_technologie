from django.views.decorators.csrf import csrf_exempt
from models import player
from forms import PlayerForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

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
            request.user.username = form.cleaned_data['username']
            request.user.password1 = form.cleaned_data['password1']
            request.user.email = form.cleaned_data['email']

            if len(form.cleaned_data['password1']) > 0:
                request.user.set_password(form.cleaned_data['password1'])

            request.user.save()
            profile.save()
            saved = True
            return HttpResponseRedirect('/accounts/profile/saved/')
    else:
        form = PlayerForm(initial={'username': request.user.username,
                                   'first_name': request.user.first_name,
                                   'last_name': request.user.last_name,
                                   'city': profile.city,
                                   'street': profile.street,
                                   'email': request.user.email,
                                   'phone': profile.phone,
        })

    return render_to_response('players/profile.html', {'form': form, 'saved': saved}, context_instance=RequestContext(request))
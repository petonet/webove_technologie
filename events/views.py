# -*- coding: utf-8 -*-
import datetime
from models import Event
#from django.contrib.gis.geoip import GeoIP
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, RequestContext, render
from django.contrib.auth.decorators import login_required
from forms import NewForm
from models import Comments
from models import player
from grounds.models import ground
from players.models import player
from django.contrib.auth.models import User
from django.utils import formats


def eventDetail(request, pk):
    if request.is_ajax():
        action = request.POST['operation']
        event = Event.objects.get(id=request.POST['eventId'])
        response = ""
        if action == "SignUp":
            #currentPlayer = request.user.player
            event.users.add(request.user.player)
            event.save()
            if request.user.player.photo._file == None:
                photo = '/media/templates_img/user.png'
            else:
                photo = "/media/uploads/image/players/" + request.user.player.photo._file


            response = '<div id="ed_player'+ str(request.user.player.id) + '">' \
		        '<div class="ed_playerSeparatorTop"></div>' \
		        '<div class="ed_player">' \
		        	'<div class="ed_playerPhotoDiv">' \
		        		'<img class="ed_playerPhoto" src="' + photo + '" </img>' \
		           '</div>' \
		           '<div class="ed_playerName">' \
		        	    '<span id="ed_playerNameText">' + request.user.username + '</span>' \
		           '</div>' \
		        '</div>' \
		        '<div class="ed_playerSeparatorBottom"></div>' \
                '</div>'

        elif action == "Unsign":
            #currentPlayer = player.objects.get(id=request.user.id)
            event.users.remove(request.user.player)
            event.save()
            response = 'Boli ste odhlásený z tejto akcie'
        elif action == "Delete":
            event.delete()
            response = "Deleted"
        elif action == "NewComment":
            comment = request.POST['comment']
            coment = Comments(eventId=event, user=request.user.player, comment=comment, sent=datetime.datetime.now())
            coment.save()
            if request.user.player.photo._file == None:
                photo = '/media/templates_img/user.png'
            else:
                photo = "/media/uploads/image/players/" + request.user.player.photo._file

            response = '<div class="ed_comment">' \
                        '<div class="ed_commentPhotoDiv">' \
                            '<img class="ed_commentPhoto"' \
                                'src="' + photo + '">' \
                          '</img>' \
                        '</div>' \
                        '<div class="ed_commentContentDiv">' \
                           ' <div class="ed_ccTop">' \
                                '<div class="ccTopName">' + coment.user.user.username + '</div>' \
                                '<div class="ccTopDate">' + coment.sent.strftime("%d.%m.%Y %H:%M") + '</div>' \
                            '</div>' \
                           ' <div class="ed_ccBottom">' \
                               '' + coment.comment + '' \
                            '</div>' \
                        '</div>' \
                    '</div>'
        else:
            response = "Error"

        return HttpResponse(response)
    else:
        context = {}

        event = Event.objects.get(id = pk)

        context['mapHeight'] = 300
        context['mapWidth'] = 600
        context['mapZoomLevel'] = 12

        naive = event.login_since.replace(tzinfo=None)
        difference = datetime.datetime.now() - naive
        if (difference.total_seconds() > 0):
            context['signAllowed'] = True
        else:
            context['signAllowed'] = False

        context['isAuthor'] = False
        context['isSigned'] = False

        if request.user.is_authenticated():
            context['authenticated'] = True
            user = request.user
            if event.author.id == user.id:
                context['isAuthor'] = True
            try:
                event.users.get(id=user.player.id)
                context['isSigned'] = True
            except:
                context['isSigned'] = False
        else:
            context['authenticated'] = False

        comments = []
        for comment in Comments.objects.all().filter(eventId=event.id).order_by('sent'):
            comments.append(comment)
            context['comments'] = comments

        context['event'] = event
        context['numberInc'] = event.users.count() + 1

        return render_to_response('event/detail.html', context, context_instance=RequestContext(request))


#class EventDetailView(generic.DetailView):
#    model = Event
#    template_name = 'event/detail.html'
#    queryset = Event.objects.all()
#
#    def get_context_data(self, **kwargs):
#        context={}
#        context['event'] = get_object_or_404(self.model, pk=self.kwargs['pk'])
#        return context


class EventsView(generic.ListView):
    model = Event
    template_name = 'event/events.html'

    def get_context_data(self, **kwargs):
        events = []
        context = {}
        for event in Event.objects.all().order_by('published'):
            events.append(event)
            context['events'] = events
        return context


def MapView(request):

    if request.is_ajax():
        context = {}
        #context['mapform'] = MapForm(initial={'map': gmap})
        #events = []
        #for event in Event.objects.all():
        #    events.append(event)
        return HttpResponse("OK")
    else:
        context = {}
        #client_address = request.META['REMOTE_ADDR']
        #context['mapform'] = MapForm(initial={'map': gmap})
        #events = []
        #for event in Event.objects.all():
        #    events.append(event)
        #context['event'] = Event.objects.get(pk=1)
        context['mapHeight'] = 500
        context['mapWidth'] = 500
        context['mapCenterLat'] = 48.998465
        context['mapCenterLng'] = 21.239812
        context['mapZoomLevel'] = 13

        events = []
        for event in Event.objects.all():
            events.append(event)
            context['events'] = events
        return render_to_response('event/mapTest.html', context, context_instance=RequestContext(request))


@login_required
def add(request):

    context = {}
    context['mapHeight'] = 500
    context['mapWidth'] = 500
    context['mapCenterLat'] = 48.998465
    context['mapCenterLng'] = 21.239812
    context['mapZoomLevel'] = 13

    grounds = []
    for grnd in ground.objects.all():
        grounds.append(grnd)
        context['grounds'] = grounds

    saved = None

    user = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        form = NewForm(request.POST, files=request.FILES)

        if form.is_valid():
            event = Event(title = form.cleaned_data['title'])

            startDate = form.cleaned_data['startOfActionDate']
            startTime = form.cleaned_data['startOfActionTime']
            splitStartDate = startDate.split(".")
            splitStartTime = startTime.split(":")
            event.startOfAction = datetime.datetime(int(float(splitStartDate[2])), int(float(splitStartDate[1])), int(float(splitStartDate[0])),
                                              int(float(splitStartTime[0])), int(float(splitStartTime[1])))

            event.published = datetime.datetime.now()
            event.numberOfPlayers = form.cleaned_data['numberOfPlayers']

            loginDate = form.cleaned_data['login_sinceDate']
            loginTime = form.cleaned_data['login_sinceTime']
            splitLoginDate = loginDate.split(".")
            splitLoginTime = loginTime.split(":")
            event.login_since = datetime.datetime(int(float(splitLoginDate[2])), int(float(splitLoginDate[1])), int(float(splitLoginDate[0])),
                                              int(float(splitLoginTime[0])), int(float(splitLoginTime[1])))

            event.prologue = form.cleaned_data['prologue']
            event.scenario = form.cleaned_data['scenario']
            event.organizationNotes = form.cleaned_data['organizationNotes']

            durationTime = form.cleaned_data['duration']
            splitDurationTime = durationTime.split(":")

            event.duration = datetime.time(int(float(splitDurationTime[0])), int(float(splitDurationTime[1])), 0)
            event.entryFee = form.cleaned_data['entryFee']
            event.author = user
            event.ground = form.cleaned_data['ground']
            event.locationLat = form.data['Latitude']
            event.locationLng = form.data['Longitude']
            event.titleImage = form.cleaned_data['titleImage']
            event.published = datetime.datetime.now()
            event.save()
            event.users.add(user.player)
            return HttpResponseRedirect('/events/detail/' + str(event.id))
        else:
            context['form'] = form
            context['fail'] = True
            return render_to_response('event/newEvent.html', context, context_instance=RequestContext(request))
    else:
        form = NewForm()
        context['form'] = form
        context['saved'] = saved
        return render_to_response('event/newEvent.html', context, context_instance=RequestContext(request))
# Create your views here.
import datetime
from models import Event
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, RequestContext, render
from django.contrib.auth.decorators import login_required
from forms import NewForm
from models import player
from django.contrib.auth.models import User
from gmapi import maps
from forms import MapForm


class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'event/detail.html'
    queryset = Event.objects.all()

    def get_context_data(self, **kwargs):
        context={}
        context['event'] = get_object_or_404(self.model, pk=self.kwargs['pk'])
        return context


class EventsView(generic.ListView):
    model = Event
    template_name = 'event/events.html'

    def get_context_data(self, **kwargs):
        events = []
        context = {}
        for event in Event.objects.all():
            events.append(event)
            context['events'] = events
        return context


def MapView(request):

    if request.is_ajax():
        return HttpResponse("This is response from server. Received title:" + request.POST['title'])
    else:
        context = {}
        gmap = maps.Map(opts = {
            'center': maps.LatLng(38, -97),
            'mapTypeId': maps.MapTypeId.ROADMAP,
            'zoom': 3,
            'mapTypeControlOptions': {
                 'style': maps.MapTypeControlStyle.DROPDOWN_MENU
            },
        })

        marker = maps.Marker(opts = {
            'map': gmap,
            'position': maps.LatLng(38, -97),
        })
        maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
        maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
        info = maps.InfoWindow({
            'content': 'Hello!',
            'disableAutoPan': True
        })
        info.open(gmap, marker)

        context['mapform'] = MapForm(initial={'map': gmap})
        #events = []
        #for event in Event.objects.all():
        #    events.append(event)
        context['event'] = Event.objects.get(pk=1)
        return render_to_response('event/mapTest.html', context, context_instance=RequestContext(request))

    #def get_context_data(self, **kwargs):
    #    events = []
#
    #    context.
    #    for event in Event.objects.all():
    #        events.append(event)
    #        context['events'] = events
    #    return context


@login_required
def add(request):

    saved = None

    user = User.objects.get(id=request.user.id)
    play = player.objects.get(user=user)

    if request.method == 'POST':
        form = NewForm(request.POST)

        if form.is_valid():
            event = Event(title = form.cleaned_data['title'])
            event.startOfAction = datetime.datetime(2000, 10, 10, 10, 10, 10, 10)
            event.published = datetime.datetime(2000, 10, 10, 10, 10, 10, 10)
            event.numberOfPlayers = form.cleaned_data['numberOfPlayers']
            event.login_since = datetime.datetime(2000, 10, 10)
            event.prologue = form.cleaned_data['prologue']
            event.scenario = form.cleaned_data['scenario']
            event.organizationNotes = form.cleaned_data['organizationNotes']
            event.duration = datetime.time(0, 0, 0)
            event.entryFee = form.cleaned_data['entryFee']
            event.author = play
            event.ground = form.cleaned_data['ground']
            event.save()
            saved = True
        return render_to_response('event/newEvent.html', {'form': form, 'saved': saved }, context_instance=RequestContext(request))

    else:
        form = NewForm()
        return render_to_response('event/newEvent.html', {'form': form, 'saved': saved }, context_instance=RequestContext(request))


def map(request):
    gmap = maps.Map(opts = {
        'center': maps.LatLng(38, -97),
        'mapTypeId': maps.MapTypeId.ROADMAP,
        'zoom': 3,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },
    })

    marker = maps.Marker(opts = {
        'map': gmap,
        'position': maps.LatLng(38, -97),
    })
    maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
    maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
    info = maps.InfoWindow({
        'content': 'Hello!',
        'disableAutoPan': True
    })
    info.open(gmap, marker)

    context = {'mapform': MapForm(initial={'map': gmap})}
    return render_to_response('event/map.html', context)
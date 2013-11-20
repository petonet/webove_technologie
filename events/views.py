# Create your views here.
import models
from models import Event
from django.views import generic


class DetailView(generic.DetailView):
    model= Event
    template_name = 'event/detail.html'
    context_object_name = "event"
    def get_queryset(self):
        return Event.objects.filter(pk=self.pk)

class EventsView(generic.ListView):
    model = Event
    template_name = 'event/events.html'


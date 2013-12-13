
from django import template
from events.models import Event

register = template.Library()

def nav_eventlist():
        events = Event.objects.all().order_by('-startOfAction')[:4]
        return {'events': events}

register.inclusion_tag('tags/events.html')(nav_eventlist)
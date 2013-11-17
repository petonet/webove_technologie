
from django import template
from grounds.models import ground

register = template.Library()

def nav_groundlist():
        grounds = ground.objects.all().order_by('-pubDate')[:5]
        return {'grounds': grounds}

register.inclusion_tag('tags/ground.html')(nav_groundlist)
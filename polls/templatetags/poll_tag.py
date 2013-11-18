from django import template
from polls.models import Poll
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import Context
from django.contrib.auth.models import validators


register = template.Library()

@login_required
def nav_detailankety(context):

    #session_data.get('_auth_user_id')
    #user = User.objects.get(id=uid)
    #User.objects.all()
    #print related_user(self,context)

    polls = Poll.objects.all().order_by('-question')

    return {'polls': polls}


register.inclusion_tag('tags/poll_detail.html',takes_context=True)(nav_detailankety)


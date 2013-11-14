# Create your views here.
from django.shortcuts import render
from models import ground
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic



#class IndexView(generic.ListView):
#    template_name = 'grounds/index.html'
#    context_object_name = 'grounds_list'
#
#    def get_queryset(self):
#        return  ground.objects.all().order_by('-pub_date')[:5]
#

class DetailView(generic.DetailView):
    model= ground
    template_name = 'grounds\\detail.html'
    context_object_name = 'grounds_list'



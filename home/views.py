# Create your views here.

from django.shortcuts import render
from grounds.models import ground
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic



class HomeView(generic.ListView):
    model = ground
    template_name = 'homepage\\homepage.html'
    #context_object_name = "homepage_list"

    #def get_queryset(self):
    #    return  ground.objects.all().order_by('-pubDate')[:5]

#    def get_context_data(self, **kwargs):
 #       context = super(PageView, self).get_context_data(**kwargs)
  #      context['more_model_objects'] = YourModel.objects.all()
  #      return context


#class DetailView(generic.DetailView):
#    model= ground
#    template_name = 'grounds/ground_detail.html'



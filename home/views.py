# Create your views here.

from django.shortcuts import render, render_to_response, RequestContext
from grounds.models import ground
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic



def HomeView(request):
    context = {}
    context['mapHeight'] = 500
    context['mapWidth'] = 1583
    context['mapCenterLat'] = 48.735965
    context['mapCenterLng'] = 19.662094
    context['mapZoomLevel'] = 8

    grounds = []
    for grnd in ground.objects.all():
        grounds.append(grnd)
        context['grounds'] = grounds

    return render_to_response('homepage/homepage.html', context, context_instance=RequestContext(request))




    #model = ground
    #template_name = 'homepage\\homepage.html'


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



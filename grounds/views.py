from models import ground
from django.views.generic import DetailView , ListView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from forms import *
import datetime
import sys


import models

class GroundDetailView(ListView):
    model= ground
    template_name = 'grounds/ground_detail.html'
    queryset = ground.objects.all()


    def get_context_data(self, **kwargs):
        context={}
        a = get_object_or_404(self.model,pk=self.kwargs['pk'])
        context['ground'] =a
        return context


class GroundsOverview(ListView):
    model = ground
    template_name = 'grounds/grounds.html'

    def get_context_data(self, **kwargs):
        a = []
        context={}
        for g in ground.objects.all():
            print g
            a.append(g)
            context['grounds'] = a

        return context


class GroundCreate(CreateView):
    model = ground
    form_class = AddGroundForm
    success_url = '/thanks/'
    template_name = 'grounds/addForm.html'
    fields = ['name,city,street,description,rate,official,photo']
    lng=None
    lat=None


    def form_valid(self, form):
        print self.request.user
        form.instance.user = self.request.user

        form.instance.locationLat=form.data['Latitude']
        form.instance.locationLng=form.data['Longitude']
        return super(GroundCreate, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(GroundCreate, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['mapHeight']=300
        context['mapWidth']=620
        context['mapZoomLevel']=7
        context['mapCenterLat']=48.73627700
        context['mapCenterLng']=19.14619170
        return context




class GroundUpdate(UpdateView):
    model = ground
    template_name = 'grounds/addForm.html'
    form_class = AddGroundForm
    success_url = '/thanks/'
    fields = ['name,city,street,description,rate,official,photo']
    #template_name_suffix = '_update_form'

    #def get_object(self, queryset=None):
    #    obj = get_object_or_404(self.model,pk=self.kwargs['pk'])
    #    print obj.name
    #    return obj



    #def form_valid(self, form):
    #    #print(self.photo)
    #    return super(GroundUpdate, self).form_valid(form)

    #
    #def get_context_data(self, **kwargs):
    #    a = get_object_or_404(self.model,pk=self.kwargs['pk'])
    #    if self.request.user is a.user:
    #        context = super(GroundCreate, self).get_context_data(**kwargs)
    #        #context['user'] = self.request.user
    #        #context['photo']=self.request.FILES['photo']
    #        return context


class GroundDelete(DeleteView):
    template_name = 'grounds/delete.html'
    model = ground
    success_url = '/grounds/'
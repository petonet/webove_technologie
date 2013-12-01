from models import ground
from django.views.generic import DetailView , ListView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from form import *
import datetime


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
            context['ground'] = a

        return context


class GroundCreate(CreateView):
    model = ground
    form_class = AddGroundForm
    success_url = '/thanks/'
    template_name = 'grounds/addForm.html'
    fields = ['name,city,street,description,rate,official,photo']



    def form_valid(self, form):
        print self.request.user
        form.instance.user = self.request.user
        #print(self.photo)
        return super(GroundCreate, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(GroundCreate, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        #context['photo']=self.request.FILES['photo']
        return context






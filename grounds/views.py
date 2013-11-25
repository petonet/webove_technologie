from models import ground
from django.views.generic import DetailView , ListView
from django.shortcuts import get_object_or_404

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






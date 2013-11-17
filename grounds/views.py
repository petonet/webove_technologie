from models import ground
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

import models

class GroundDetailView(DetailView):
    model= ground
    template_name = 'grounds/detail.html'
    #queryset = ground.objects.all()


    #def get_object(self,queryset=None):
    #    pk=self.pk_url_kwarg.get("pk")
    #    print pk
    #    groundObj = get_object_or_404(ground, pk)
    #    return  groundObj






from models import ground
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

import models

class GroundDetailView(DetailView):
    model= ground
    template_name = 'grounds/ground_detail.html'
    queryset = ground.objects.all()
    context_object_name = "ground_detail"




    def get_object(self,queryset=None):
        pk=self.args[0]
        print pk
        groundObj = get_object_or_404(ground, pk)
        return  groundObj






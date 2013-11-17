# Create your views here.
import models
from models import Event


class DetailView(models.generic.DetailView):
    model= Event
    template_name = 'event/detail.html'
    context_object_name = "event"
    def get_queryset(self):
        return Event.objects.filter(pk=self.pk)

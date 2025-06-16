from rest_framework import generics
from .models import Event
from .serializers import EventSerializer

class EventListCreateView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
class EventUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True  # This ensures PATCH-like behavior even on PUT
        return super().update(request, *args, **kwargs)

    
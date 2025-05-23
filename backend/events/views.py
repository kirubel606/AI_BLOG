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
    
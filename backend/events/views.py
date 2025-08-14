from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly
from .models import Event
from .serializers import EventSerializer

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # Only authenticated users can create; everyone can read
    permission_classes = [ DjangoModelPermissionsOrAnonReadOnly]

class EventUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly]

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True  # Allow partial updates
        return super().update(request, *args, **kwargs)
from rest_framework import generics, status
from .models import Event
from .serializers import EventSerializer
from django.contrib.auth.models import Permission

from rest_framework.response import Response
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        if not request.user.has_perm('events.add_event'):
            return Response(
                {"detail": "You do not have permission to create events."},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().create(request, *args, **kwargs)

class EventUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        if not request.user.has_perm('events.change_event'):
            return Response(
                {"detail": "You do not have permission to update events."},
                status=status.HTTP_403_FORBIDDEN
            )
        kwargs['partial'] = True  # Allow partial update
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not request.user.has_perm('events.delete_event'):
            return Response(
                {"detail": "You do not have permission to delete events."},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)
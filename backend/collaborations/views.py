from rest_framework import generics
from rest_framework.permissions import BasePermission
from .models import Collaboration
from .serializers import CollaborationSerializer


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow safe methods for everyone
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True
        # Only staff/admins can modify
        return request.user and request.user.is_staff


class CollaborationListCreateView(generics.ListCreateAPIView):
    queryset = Collaboration.objects.all()
    serializer_class = CollaborationSerializer
    permission_classes = [IsAdminOrReadOnly]


class CollaborationUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collaboration.objects.all()
    serializer_class = CollaborationSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

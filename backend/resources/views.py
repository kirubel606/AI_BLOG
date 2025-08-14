from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, BasePermission
from .models import Resource
from .serializers import ResourceSerializer


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    Read-only for everyone; write actions require authentication.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


class ResourcesListCreateView(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ResourcesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

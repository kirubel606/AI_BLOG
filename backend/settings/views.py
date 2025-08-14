from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, BasePermission
from .models import Setting
from .serializers import SettingsSerializer


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    Read-only for everyone; write actions require authentication.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


class SettingsListCreateView(generics.ListCreateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SettingsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

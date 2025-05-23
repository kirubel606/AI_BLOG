from rest_framework import generics
from .models import Setting
from .serializers import SettingsSerializer

class SettingsListCreateView(generics.ListCreateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingsSerializer

class SettingsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingsSerializer
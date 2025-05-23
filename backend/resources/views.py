from rest_framework import generics
from .models import Resource
from .serializers import ResourceSerializer

class ResourcesListCreateView(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class ResourcesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
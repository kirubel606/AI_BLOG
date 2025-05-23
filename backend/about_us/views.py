from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import AboutUs
from .serializers import AboutUsSerializer

class AboutUsListCreateView(generics.ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AboutUsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
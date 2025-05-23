from rest_framework import generics
from .models import RND  # Make sure you have a model named Rnd
from .serializers import RndSerializer  # Make sure you have a serializer for Rnd

class RndListCreateView(generics.ListCreateAPIView):
    queryset = RND.objects.all()
    serializer_class = RndSerializer

class RndRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RND.objects.all()
    serializer_class = RndSerializer
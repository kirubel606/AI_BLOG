from rest_framework import generics
from .models import Collaboration
from .serializers import CollaborationSerializer

class CollaborationListCreateView(generics.ListCreateAPIView):
    queryset = Collaboration.objects.all()
    serializer_class = CollaborationSerializer

class CollaborationUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collaboration.objects.all()
    serializer_class = CollaborationSerializer
    lookup_field = 'pk'
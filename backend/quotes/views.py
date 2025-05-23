from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Quote
from .serializers import QuoteSerializer

class QuoteListCreateView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class QuoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
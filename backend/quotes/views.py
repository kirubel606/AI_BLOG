from rest_framework import generics
from .models import Quote
from .serializers import QuoteSerializer

class QuoteListCreateView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    def get_queryset(self):
        return Quote.objects.filter(is_testimony=False)

class QuoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    
class TestimonialListView(generics.ListAPIView):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        return Quote.objects.filter(is_testimony=True)

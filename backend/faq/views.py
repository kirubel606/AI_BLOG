from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import FAQ
from .serializers import FAQSerializer

class FAQListCreateView(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FAQRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True  # 👈 enables partial update
        return super().update(request, *args, **kwargs)
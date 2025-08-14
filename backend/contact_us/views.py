from rest_framework import generics
from .models import ContactUs
from .serializers import ContactUsSerializer
from .models import EmailSubscription
from .serializers import EmailSubscriptionSerializer

class ContactUsListCreateView(generics.ListCreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

class ContactUsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    lookup_field = 'pk'

class EmailSubscriptionView(generics.CreateAPIView):
    queryset = EmailSubscription.objects.all()
    serializer_class = EmailSubscriptionSerializer
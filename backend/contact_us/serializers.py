from rest_framework import serializers
from .models import ContactUs
from .models import EmailSubscription

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


class EmailSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSubscription
        fields = ['id', 'email', 'created_at']
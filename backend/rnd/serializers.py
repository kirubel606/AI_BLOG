from rest_framework import serializers
from .models import RND

class RndSerializer(serializers.ModelSerializer):
    class Meta:
        model = RND
        fields = '__all__'
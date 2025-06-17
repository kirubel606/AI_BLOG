# serializers.py
from rest_framework import serializers
from .models import RND

class RndSerializer(serializers.ModelSerializer):
    # Convert images comma string into list for output
    images = serializers.SerializerMethodField()

    class Meta:
        model = RND
        fields = '__all__'

    def get_images(self, obj):
        if obj.images:
            return obj.images.split(',')
        return []

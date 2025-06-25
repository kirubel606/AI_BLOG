from rest_framework import serializers
from .models import Event, EventImage

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ['id', 'image']

class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            'id', 'title','title_am', 'location','location_am', 'description','description_am', 'category', 'venue','venue_am',
            'video_link', 'is_live', 'timestamp', 'start_date', 'end_date',
            'type', 'status', 'images'
        ]

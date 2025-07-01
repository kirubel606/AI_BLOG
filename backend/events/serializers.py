from rest_framework import serializers
from .models import Event, EventImage
from urllib.parse import urlparse

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ['id', 'image']

class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'title_am', 'location', 'location_am', 'description', 'description_am',
            'category', 'venue', 'venue_am', 'video_link', 'is_live', 'timestamp',
            'start_date', 'end_date', 'type', 'status', 'images'
        ]

    def create(self, validated_data):
        request = self.context['request']
        images_data = request.FILES.getlist('images')
        event = Event.objects.create(**validated_data)

        for image in images_data:
            EventImage.objects.create(event=event, image=image)

        return event

    def update(self, instance, validated_data):
        request = self.context['request']

        # Remove old images
        removed_images = request.data.getlist("removed_images")
        if removed_images:
            removed_paths = []
            for url in removed_images:
                parsed_url = urlparse(url)
                path = parsed_url.path
                if path.startswith("/media/"):
                    path = path[len("/media/"):]
                removed_paths.append(path)

            instance.images.filter(image__in=removed_paths).delete()

        # Add new images
        images_data = request.FILES.getlist("images")
        for image in images_data:
            EventImage.objects.create(event=instance, image=image)

        # Update fields
        for field in [
            "title", "title_am", "location", "location_am", "description",
            "description_am", "category", "venue", "venue_am", "video_link",
            "is_live", "timestamp", "start_date", "end_date", "type", "status"
        ]:
            if field in validated_data:
                setattr(instance, field, validated_data[field])

        instance.save()
        return instance

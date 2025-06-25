from rest_framework import serializers
from .models import Gallery, GalleryImage

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ["id", "image"]

class GallerySerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True, required=False)

    class Meta:
        model = Gallery
        fields = ["id", "title","title_am", "caption","caption_am","discription","discription_am", "images", "created_at"]

    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        gallery = Gallery.objects.create(**validated_data)
        for image in images_data:
            GalleryImage.objects.create(gallery=gallery, image=image)
        return gallery

    def update(self, instance, validated_data):
        request = self.context['request']

        removed_images = request.data.getlist("removed_images")
        if removed_images:
            from urllib.parse import urlparse

            removed_paths = []
            for url in removed_images:
                parsed_url = urlparse(url)
                path = parsed_url.path
                if path.startswith("/media/"):
                    path = path[len("/media/"):]
                removed_paths.append(path)

            instance.images.filter(image__in=removed_paths).delete()

        images_data = request.FILES.getlist("images")
        for image in images_data:
            GalleryImage.objects.create(gallery=instance, image=image)

        instance.title = validated_data.get("title", instance.title)
        instance.title_am = validated_data.get("title_am", instance.title)
        instance.caption = validated_data.get("caption", instance.caption)
        instance.caption_am = validated_data.get("caption_am", instance.caption_am)
        instance.discription = validated_data.get("discription", instance.discription)
        instance.discription_am = validated_data.get("discription_am", instance.discription_am)
        instance.save()

        return instance

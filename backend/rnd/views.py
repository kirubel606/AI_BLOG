# views.py
import os
from django.core.files.storage import default_storage
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from .models import RND
from .serializers import RndSerializer

class RndListCreateView(generics.ListCreateAPIView):
    queryset = RND.objects.all()
    serializer_class = RndSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        images_files = self.request.FILES.getlist("images")
        image_urls = []

        for image_file in images_files:
            path = default_storage.save(os.path.join("rnd", image_file.name), image_file)
            url = default_storage.url(path)
            image_urls.append(url)

        # Save as comma separated string
        images_str = ",".join(image_urls) if image_urls else ""

        serializer.save(images=images_str)

class RndRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RND.objects.all()
    serializer_class = RndSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_update(self, serializer):
        instance = self.get_object()
        images_files = self.request.FILES.getlist("images")
        image_urls = instance.images.split(',') if instance.images else []

        for image_file in images_files:
            path = default_storage.save(os.path.join("rnd", image_file.name), image_file)
            url = default_storage.url(path)
            image_urls.append(url)

        images_str = ",".join(image_urls) if image_urls else ""
        serializer.save(images=images_str)

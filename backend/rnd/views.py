import os
from django.core.files.storage import default_storage
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, BasePermission
from .models import RND
from .serializers import RndSerializer


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    Read-only for anyone; write actions require authentication.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


class RndListCreateView(generics.ListCreateAPIView):
    queryset = RND.objects.all()
    serializer_class = RndSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        images_files = self.request.FILES.getlist("images")
        image_urls = []

        for image_file in images_files:
            path = default_storage.save(os.path.join("rnd", image_file.name), image_file)
            url = default_storage.url(path)
            image_urls.append(url)

        images_str = ",".join(image_urls) if image_urls else ""
        serializer.save(images=images_str)


class RndRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RND.objects.all()
    serializer_class = RndSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

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

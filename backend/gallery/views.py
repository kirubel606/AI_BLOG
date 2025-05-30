from rest_framework import viewsets
from .models import Gallery
from .serializers import GallerySerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthenticatedForUnsafeMethods(BasePermission):
    """
    Allow GET/HEAD/OPTIONS for everyone, require authentication for POST/PUT/PATCH/DELETE.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all().order_by('-created_at')  # Latest first
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticatedForUnsafeMethods]

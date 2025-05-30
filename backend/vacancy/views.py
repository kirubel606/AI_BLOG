from rest_framework import viewsets
from .models import Vacancy
from .serializers import VacancySerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsAuthenticatedForUnsafeMethods(BasePermission):
    """
    Allow GET/HEAD/OPTIONS for everyone, require authentication for POST/PUT/PATCH/DELETE.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [IsAuthenticatedForUnsafeMethods]


from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission
from .models import Category
from .serializers import CategorySerializer


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True
        return request.user and request.user.is_staff


class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        path_segment = self.request.path.rstrip('/').split('/')[-1]

        if path_segment == 'core':
            return Category.objects.filter(is_core=True)
        elif path_segment == 'non-core':
            return Category.objects.filter(is_core=False)
        return Category.objects.all()


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

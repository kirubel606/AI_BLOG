from django.shortcuts import render
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer

# Create your views here.
class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        path_segment = self.request.path.rstrip('/').split('/')[-1]  # clean segment

        if path_segment == 'core':
            return Category.objects.filter(is_core=True)
        elif path_segment == 'non-core':
            return Category.objects.filter(is_core=False)
        return Category.objects.all()

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True  # 👈 enables partial update
        return super().update(request, *args, **kwargs)
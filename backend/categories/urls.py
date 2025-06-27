from django.urls import path
from .views import CategoryListCreateView, CategoryRetrieveUpdateDestroyView

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='category-list-all'),
    path('core', CategoryListCreateView.as_view(), name='category-list-core'),
    path('non-core', CategoryListCreateView.as_view(), name='category-list-non-core'),
    path('<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
]
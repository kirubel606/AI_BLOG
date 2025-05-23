from django.urls import path
from .views import ResourcesListCreateView, ResourcesRetrieveUpdateDestroyView

urlpatterns = [
    path('', ResourcesListCreateView.as_view(), name='resources-list'),
    path('<int:pk>/', ResourcesRetrieveUpdateDestroyView.as_view(), name='resources-detail'),
]
from django.urls import path
from .views import EventListCreateView, EventUpdateDestroyView

urlpatterns = [
    path('', EventListCreateView.as_view(), name='event-list'),
    path('<int:pk>/', EventUpdateDestroyView.as_view(), name='event-detail'),
]

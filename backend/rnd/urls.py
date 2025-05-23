from django.urls import path
from .views import RndListCreateView, RndRetrieveUpdateDestroyView

urlpatterns = [
    path('', RndListCreateView.as_view(), name='rnd-list'),
    path('<int:pk>/', RndRetrieveUpdateDestroyView.as_view(), name='rnd-detail'),
]
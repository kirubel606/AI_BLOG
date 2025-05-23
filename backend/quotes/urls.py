from django.urls import path
from .views import QuoteListCreateView, QuoteRetrieveUpdateDestroyView

urlpatterns = [
    path('', QuoteListCreateView.as_view(), name='quote-list'),
    path('<int:pk>/', QuoteRetrieveUpdateDestroyView.as_view(), name='quote-detail'),
]
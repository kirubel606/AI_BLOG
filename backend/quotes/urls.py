from django.urls import path
from .views import QuoteListCreateView, QuoteRetrieveUpdateDestroyView,TestimonialListView

urlpatterns = [
    path('testimonials/', TestimonialListView.as_view(), name='testimonials'),
    path('', QuoteListCreateView.as_view(), name='quote-list'),
    path('<int:pk>/', QuoteRetrieveUpdateDestroyView.as_view(), name='quote-detail'),
]
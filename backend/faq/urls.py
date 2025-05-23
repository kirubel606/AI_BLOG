from django.urls import path
from .views import FAQListCreateView, FAQRetrieveUpdateDestroyView

urlpatterns = [
    path('', FAQListCreateView.as_view(), name='faq-list'),
    path('<int:pk>/', FAQRetrieveUpdateDestroyView.as_view(), name='faq-detail'),
]
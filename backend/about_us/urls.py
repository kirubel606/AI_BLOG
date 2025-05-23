from django.urls import path
from .views import AboutUsListCreateView, AboutUsRetrieveUpdateDestroyView

urlpatterns = [
    path('', AboutUsListCreateView.as_view(), name='about_us'),
    path('<int:pk>/', AboutUsRetrieveUpdateDestroyView.as_view(), name='about_us_detail'),
] 

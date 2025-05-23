from django.urls import path
from .views import NewsListCreateView, NewsRetrieveUpdateDestroyView

urlpatterns = [
    path('', NewsListCreateView.as_view(), name='news_list'),
    path('<int:pk>/', NewsRetrieveUpdateDestroyView.as_view(), name='news_detail'),
]

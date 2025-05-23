from django.urls import path
from .views import SettingsListCreateView, SettingsRetrieveUpdateDestroyView

urlpatterns = [
    path('', SettingsListCreateView.as_view(), name='settings-list'),
    path('<int:pk>/', SettingsRetrieveUpdateDestroyView.as_view(), name='settings-detail'),
]
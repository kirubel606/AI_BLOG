from django.urls import path
from .views import CollaborationListCreateView, CollaborationUpdateDeleteView

urlpatterns = [
    path('', CollaborationListCreateView.as_view(), name='collaboration'),
    path('<int:pk>/', CollaborationUpdateDeleteView.as_view(), name='collaboration_detail'),
] 
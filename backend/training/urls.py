# training/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StartupViewSet,
    StartupProgramViewSet,
    StartupImageViewSet,
    TrainingViewSet,
    TrainingProgramViewSet,
    TrainingImageViewSet,
)

router = DefaultRouter()
router.register(r'startups', StartupViewSet, basename='startup')
router.register(r'startup-programs', StartupProgramViewSet, basename='startup-program')
router.register(r'startup-images', StartupImageViewSet, basename='startup-image')

router.register(r'trainings', TrainingViewSet, basename='training')
router.register(r'training-programs', TrainingProgramViewSet, basename='training-program')
router.register(r'training-images', TrainingImageViewSet, basename='training-image')

urlpatterns = [
    path('', include(router.urls)),
]

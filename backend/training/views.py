from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import (
    Startup, StartupProgram, StartupImage,
    Training, TrainingProgram, TrainingImage
)
from .serializers import (
    StartupCreateSerializer,
    StartupSerializer, StartupProgramSerializer, StartupImageSerializer,
    TrainingSerializer, TrainingProgramSerializer, TrainingImageSerializer
)


# ---------- STARTUP VIEWSETS ----------
class StartupViewSet(viewsets.ModelViewSet):
    queryset = Startup.objects.all().order_by("-created_at")

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return StartupCreateSerializer
        return StartupSerializer

class StartupProgramViewSet(viewsets.ModelViewSet):
    queryset = StartupProgram.objects.all().order_by("-created_at")
    serializer_class = StartupProgramSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StartupImageViewSet(viewsets.ModelViewSet):
    queryset = StartupImage.objects.all().order_by("-created_at")
    serializer_class = StartupImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ---------- TRAINING VIEWSETS ----------
class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all().order_by("-created_at")
    serializer_class = TrainingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TrainingProgramViewSet(viewsets.ModelViewSet):
    queryset = TrainingProgram.objects.all().order_by("-created_at")
    serializer_class = TrainingProgramSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TrainingImageViewSet(viewsets.ModelViewSet):
    queryset = TrainingImage.objects.all().order_by("-created_at")
    serializer_class = TrainingImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

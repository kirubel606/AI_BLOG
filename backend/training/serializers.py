from rest_framework import serializers
from .models import (
    Startup, StartupProgram, StartupImage,
    Training, TrainingProgram, TrainingImage
)


# ---------- STARTUP SERIALIZERS ----------

class StartupProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupProgram
        fields = [
            "id", "title_en", "title_am",
            "description_en", "description_am",
            "duration_en", "duration_am",
            "icon_name", "created_at", "updated_at"
        ]

class StartupImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupImage
        fields = ["id", "image", "alt_text_en", "alt_text_am", "created_at", "updated_at"]

class StartupSerializer(serializers.ModelSerializer):
    programs = StartupProgramSerializer(many=True, read_only=True)
    images = StartupImageSerializer(many=True, read_only=True)

    class Meta:
        model = Startup
        fields = [
            "id", "title_en", "title_am",
            "description_en", "description_am",
            "about_en", "about_am",
            "programs", "images",
            "created_at", "updated_at"
        ]

# Optional: Add a writable field to upload multiple images at once
class StartupCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Startup
        fields = ["id", "title_en", "title_am", "description_en", "description_am",
                  "about_en", "about_am", "images"]

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])
        startup = Startup.objects.create(**validated_data)
        for image in images_data:
            StartupImage.objects.create(startup=startup, image=image)
        return startup

# ---------- TRAINING SERIALIZERS ----------
class TrainingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingImage
        fields = ["id", "image", "alt_text_en", "alt_text_am", "created_at", "updated_at"]


class TrainingProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingProgram
        fields = [
            "id", "title_en", "title_am",
            "description_en", "description_am",
            "duration_en", "duration_am",
            "icon_name", "created_at", "updated_at"
        ]


class TrainingSerializer(serializers.ModelSerializer):
    programs = TrainingProgramSerializer(many=True, read_only=True)
    images = TrainingImageSerializer(many=True, read_only=True)

    class Meta:
        model = Training
        fields = [
            "id", "training_type",
            "title_en", "title_am",
            "description_en", "description_am",
            "about_en", "about_am",
            "programs", "images",
            "created_at", "updated_at"
        ]

from rest_framework.serializers import CharField, ImageField,SlugField, RelatedField, ModelSerializer
from news.models import  News,NewsImage
from categories.models import Category
from rest_framework.serializers import SlugRelatedField
from rest_framework import serializers
from rest_framework.fields import URLField


class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = ['id', 'image']

class NewsSerializer(ModelSerializer):
    author_username = CharField(source='author.username', read_only=True)
    author_profile_image = ImageField(source='author.profile_image', read_only=True)

    # New fields
    images = NewsImageSerializer(many=True, read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    category_am = serializers.SerializerMethodField()
    class Meta:
        model = News
        fields = [
            'id', 'title','title_am', 'slug', 'subtitle','subtitle_am', 'cover_image', 'content','content_am',
            'category','category_am' ,'created_at', 'status', 'view_count', 'author',
            'author_username', 'author_profile_image', 'images', 'iframe','tags','magazine','pdf_file'  # <--- Added here
        ]
    def get_category_am(self, obj):
        return obj.category.name_am if obj.category else None


    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        news = News.objects.create(**validated_data)

        for image in images_data:
            NewsImage.objects.create(news=news, image=image)

        return news

    def update(self, instance, validated_data):
        images_data = self.context['request'].FILES.getlist('images')

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if images_data:
            instance.images.all().delete()  # Clear existing
            for image in images_data:
                NewsImage.objects.create(news=instance, image=image)

        return instance


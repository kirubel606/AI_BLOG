from rest_framework.serializers import CharField, ImageField, SlugField, RelatedField, ModelSerializer
from news.models import  News


class NewsSerializer(ModelSerializer):

    author_username = CharField(source='author.username', read_only=True)
    author_profile_image = ImageField(
        source='author.profile_image', read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'slug', 'subtitle', 'images', 'content', 'category', 'created_at',
                  'status', 'applaud_count', 'author', 'author_username', 'author_profile_image']

    def update(self, instance, validated_data):
        # Allowed update fields are: [title, subtitle, cover_image, content, category, status]

        for key, data in validated_data.items():
            if key == 'images':
                instance.images.delete(save=False)
            setattr(instance, key, data)

        instance.save()

        return instance


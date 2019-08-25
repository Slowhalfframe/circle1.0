from rest_framework import serializers
from articles.models import Article


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ('id', 'title', 'content', 'cover_img', 'create_time', 'article_from', 'article_type')
        fields = '__all__'
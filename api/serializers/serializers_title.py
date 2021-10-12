from django.db.models import Avg
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models.category import Category
from api.models.genre import Genre
from api.models.review import Review
from api.models.title import Title
from api.models.titlegenre import TitleGenre
from api.serializers.serializers_category import CategorySerializer
from api.serializers.serializers_genre import GenreSerializer


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True,
        required=False)
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all(), required=False)

    class Meta:
        model = Title
        fields = '__all__'

    def create(self, validated_data):
        if 'genre' not in self.initial_data:
            title = Title.objects.create(**validated_data)
        else:
            genres_list = validated_data.pop('genre')
            title = Title.objects.create(**validated_data)
            for genre in genres_list:
                TitleGenre.objects.create(genre=genre, title=title)
        return title

    def update(self, title, validated_data):
        if 'name' not in self.initial_data:
            raise ValidationError(
                'Необходимо указать наименование произведения'
                ' при обновлении информации')
        if 'genre' in self.initial_data:
            genres_list = validated_data.pop('genre')
            for genre in genres_list:
                TitleGenre.objects.get_or_create(genre=genre, title=title)
        title = super().update(title, validated_data)
        return title


class TitleListSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    genre = GenreSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category')

    def get_rating(self, title):
        reviews = Review.objects.filter(title=title)
        rating = reviews.aggregate(average_score=Avg('score'))
        rating = rating['average_score']
        if rating is not None:
            rating = round(rating, 1)
        return rating

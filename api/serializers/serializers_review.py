from rest_framework import serializers

from api.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    def validate(self, data):
        review = Review.objects.filter(title=self.context['title'],
                                       author=self.context['author'])
        if review.exists() and self.context['request.method'] == 'POST':
            raise serializers.ValidationError(
                'Вы уже писали отзыв на это произведение.'
            )
        return data

    class Meta:
        model = Review
        exclude = ['title']

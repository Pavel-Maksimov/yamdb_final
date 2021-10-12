from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.models.comment import Comment
from api.models.review import Review
from api.models.title import Title
from api.permissions import IsAuthorOrStaff
from api.serializers.serializers_comment import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    View to CRUD comments.
    * Safe methods are available for Anonymous,
    others - for comment's author or staff only.
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrStaff]

    def get_queryset(self, *args, **kwargs):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        title = get_object_or_404(Title, id=title_id)
        review = get_object_or_404(Review, id=review_id, title=title)
        return Comment.objects.filter(review=review)

    def perform_create(self, serializer, *args, **kwargs):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        serializer.save(author=self.request.user, review=review)

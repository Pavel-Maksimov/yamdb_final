from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.filters.filter_titles import TitleFilter
from api.models.title import Title
from api.permissions import IsAdminOrReadOnly
from api.serializers.serializers_title import (TitleListSerializer,
                                               TitleSerializer)


class TitleViewSet(ModelViewSet):
    """
    View to CRUD titles.

    * Safe methods are available for Anonymous,
    others - for authenticated admin only.
    """
    queryset = Title.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return TitleListSerializer
        return TitleSerializer

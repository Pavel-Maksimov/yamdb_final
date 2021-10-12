from rest_framework import filters, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from api.models.genre import Genre
from api.permissions import IsAdminOrReadOnly
from api.serializers.serializers_genre import GenreSerializer


class ListCreateDestroyViewSet(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               mixins.DestroyModelMixin,
                               GenericViewSet):
    pass


class GenreViewSet(ListCreateDestroyViewSet):
    """
    View to create, list and destroy genres.

    * List method is available for Anonymous,
    others - for authenticated admin only.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'

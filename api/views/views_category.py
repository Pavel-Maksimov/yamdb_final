from rest_framework import filters, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from api.models.category import Category
from api.permissions import IsAdminOrReadOnly
from api.serializers.serializers_category import CategorySerializer


class ListCreateDestroyViewSet(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               mixins.DestroyModelMixin,
                               GenericViewSet):
    pass


class CategoryViewSet(ListCreateDestroyViewSet):
    """
    View to create, list and destroy categories.

    * List method is available for Anonymous,
    others - for authenticated admin only.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'

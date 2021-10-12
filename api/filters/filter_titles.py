import django_filters

from api.models.title import Title


class TitleFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name', lookup_expr='icontains')
    year = django_filters.NumberFilter(
        field_name='year', lookup_expr='iexact')
    genre = django_filters.CharFilter(
        field_name='genre__slug', lookup_expr='iexact')
    category = django_filters.CharFilter(
        field_name='category__slug', lookup_expr='iexact')

    class Meta:
        model = Title
        fields = ('name', 'year', 'genre', 'category')

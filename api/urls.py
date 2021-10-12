from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.authentication.views import JWTTokenView, RegisterView
from api.views.views_category import CategoryViewSet
from api.views.views_comment import CommentViewSet
from api.views.views_genre import GenreViewSet
from api.views.views_review import ReviewViewSet
from api.views.views_title import TitleViewSet
from api.views.views_user import YaUserViewSet

router_v1 = DefaultRouter()

router_v1.register('v1/categories', CategoryViewSet, basename='categories')
router_v1.register('v1/genres', GenreViewSet, basename='genres')
router_v1.register('v1/titles', TitleViewSet, basename='titles')
router_v1.register('v1/users', YaUserViewSet, basename='users')
router_v1.register(
    r'v1/titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'v1/titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('', include(router_v1.urls)),
    path(
        'v1/auth/email/',
        RegisterView.as_view(),
        name='registration'),
    path(
        'v1/auth/token/',
        JWTTokenView.as_view(),
        name='token_obtain_pair'
    )
]

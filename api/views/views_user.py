from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models.user import YaUser
from api.permissions import IsAdmin
from api.serializers.serializers_user import YaUserSerializer


class YaUserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    by users with 'admin' role only.
    * 'users/me/' endpoint shows and updates info about current user and
    is availiable for all authenticated.
    """
    queryset = YaUser.objects.all()
    serializer_class = YaUserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    lookup_field = 'username'

    @action(detail=False, methods=['get', 'patch'],
            permission_classes=[IsAuthenticated])
    def me(self, request):
        user = self.request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        if request.method == 'PATCH':
            serializer = self.get_serializer(
                user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)

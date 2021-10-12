from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from api.models.user import YaUser

USER_ERROR = {
    'error': 'Пользователь с таким email уже существует!'
}
CODE_INFO = {
    'email': 'Код подтверждения отправлен на Ваш email!'
}
CODE_ERROR = {
    'error': 'Неверный код подтверждения'
}


def get_tokens_for_user(user):
    """Create new refresh and access tokens for given user."""
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterView(APIView):
    """Provide confirmation code to user for given email."""
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        user = YaUser.objects.filter(email=email).exists()
        if user:
            return Response(
                USER_ERROR, status=status.HTTP_400_BAD_REQUEST
            )
        user = YaUser.objects.create_user(
            username=email, email=email, password=None
        )
        confirmation_code = default_token_generator.make_token(user)
        send_mail(
            'Ваш код подтверждения',
            confirmation_code,
            settings.DEFAULT_FROM_EMAIL,
            (email,),
        )
        return Response(CODE_INFO, status=status.HTTP_200_OK)


class JWTTokenView(APIView):
    """Provide token to user for given email and confirmation_code."""
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data['email']
        confirmation_code = request.data['confirmation_code']
        user = get_object_or_404(YaUser, email=email)
        if not default_token_generator.check_token(
            user, confirmation_code
        ):
            return Response(
                CODE_ERROR, status=status.HTTP_400_BAD_REQUEST
            )
        response = get_tokens_for_user(user)
        return Response(response, status=status.HTTP_200_OK)

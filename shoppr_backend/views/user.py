import json
import logging

from ..models import User
from ..models import RefreshToken as RefreshTokenModel

from ..serializers.UserSerializer import UserSerializer

from datetime import timezone
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.utils import timezone

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

logger = logging.getLogger("django")


class Register(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request: Request, *args, **kwargs) -> JsonResponse:
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return JsonResponse(
                data={"message": "Successfully created user"},
                status=status.HTTP_201_CREATED
            )
        except ValidationError:
            return JsonResponse(
                data={'error': 'User with this username already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logger.error(msg=f'Unexpected error: {e}', exc_info=True)
            return JsonResponse(
                data={'error': f'Unable to create user'},
                status=status.HTTP_400_BAD_REQUEST
            )


class Login(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request: Request, *args, **kwargs) -> JsonResponse:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse(data={'error': 'Invalid JSON'}, status=status.HTTP_400_BAD_REQUEST)

        if not all(data.get(field) for field in ['username', 'password']):
            return JsonResponse(data={'error': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)

        username = request.data["username"]
        password = request.data["password"]

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            return JsonResponse(data={"error": "User does not exist"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if not check_password(password, user.password):
            return JsonResponse(data={'error': 'Incorrect Password'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])

        refresh = RefreshToken.for_user(user)

        response = JsonResponse(data={'token': str(refresh.access_token)})
        RefreshTokenModel.objects.create(user=user, refresh_token=str(refresh))
        response.set_cookie(
            key='refresh_token',
            value=str(refresh),
            httponly=True,
            secure=settings.SESSION_COOKIE_SECURE,
            samesite='Lax'
        )
        return response

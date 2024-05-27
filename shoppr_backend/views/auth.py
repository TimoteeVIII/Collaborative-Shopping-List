from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken as rt
from ..models import RefreshToken, User
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes


class RefreshTokenView(View):

    @staticmethod
    def create_or_update_refresh_token(user: User) -> None:
        existing_refresh_token = RefreshToken.objects.filter(user=user).first()

        if existing_refresh_token:
            existing_refresh_token.refreshToken = rt.for_user(user)
            existing_refresh_token.save()
        else:
            RefreshToken.objects.create(
                user=user,
                refreshToken=rt.for_user(user),
                active=True,
                expires_at=None,
            )


@permission_classes([IsAuthenticated])
class AccessTokenView(APIView):

    @staticmethod
    def get(request) -> HttpResponse:
        return JsonResponse({"message": request.user.id}, status=200)

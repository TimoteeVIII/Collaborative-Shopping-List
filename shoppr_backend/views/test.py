from django.http import HttpRequest, HttpResponse
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class TestView(APIView):
    # permission_classes = [IsAuthenticated]

    @staticmethod
    @permission_classes([IsAuthenticated])
    def get(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return HttpResponse("This is a test")

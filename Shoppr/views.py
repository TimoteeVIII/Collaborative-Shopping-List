from django.http import HttpRequest, HttpResponse
from django.views import View


class HealthProcessorView(View):

    @staticmethod
    def get(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return HttpResponse("Healthy")

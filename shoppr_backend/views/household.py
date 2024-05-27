from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
import json

from ..models import Household
from .. models import User


class HouseholdViews(View):

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        raise NotImplementedError

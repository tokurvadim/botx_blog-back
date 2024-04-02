from rest_framework.views import APIView

from core.models import Page
from services.CustomRoute import TelegraphSaveRoute


class GetPage(APIView):
    def get(self, request):
        pass
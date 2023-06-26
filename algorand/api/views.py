import os

from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from algorand.settings import STATICFILES_DIRS

from .serializers import *


class GraphicView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            param = request.GET.get('parameter')
            file_path = STATICFILES_DIRS[0] + f'/algos/img/Perfomance_{param}.png'
            print(file_path)
            with open(file_path, 'rb') as f:
                image_data = f.read()

            return HttpResponse(image_data, content_type='image/png')

        except Exception as error:
            return Response({'error': error.args[1]}, status=404)

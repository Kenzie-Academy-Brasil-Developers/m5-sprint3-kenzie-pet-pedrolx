from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status

from traits.models import Trait

class TraitViews(APIView):
    def get(self, request: Request) -> Response:

        traits = Trait.objects.all()

        return Response(traits, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        return Response({'data': 'post'})

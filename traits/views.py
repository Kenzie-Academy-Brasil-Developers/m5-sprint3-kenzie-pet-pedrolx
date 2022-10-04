from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status

class TraitViews(APIView):
    def get(self, request: Request) -> Response:
        return Response({'data': 'get'})

    def post(self, request: Request) -> Response:
        return Response({'data': 'post'})

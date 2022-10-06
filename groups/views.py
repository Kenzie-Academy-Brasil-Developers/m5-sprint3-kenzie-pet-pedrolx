from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status

from groups.models import Group

class GroupViews(APIView):
    def get(self, request: Request) -> Response:

        groups = Group.objects.all()

        return Response(groups, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        return Response({'data': 'post'})

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from app.models import UserModel
from app.serializers import UserSerializer

# Create your views here.

class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = UserModel.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class 
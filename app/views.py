from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, exceptions
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from app.models import UserModel, BienesModel
from app.serializers import UserSerializer, BienesSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.contrib.auth.hashers import make_password

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    User = get_user_model()
    username = request.data.get("username")
    password = request.data.get("password")

    response = Response()

    if username is None or password is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return response

    user = User.objects.filter(username=username).first()
    if user is None:
        raise exceptions.AuthenticationFailed('user not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('invalid password')

    user_serializer = UserSerializer(user).data

    access = AccessToken.for_user(user)
    refresh = RefreshToken.for_user(user)

    response.data = {
        'access_token': str(access),
        'refresh_token': str(refresh),
        'user': user_serializer
    }

    return response

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    fullname = request.data.get("fullname")
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    response = Response()

    if fullname is None or username is None or email is None or password is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return response

    user = UserModel.objects.create(fullname=fullname, username=username, email=email, password=make_password(password))

    user_serializer = UserSerializer(user).data
    access = AccessToken.for_user(user)
    refresh = RefreshToken.for_user(user)

    response.data = {
        'access_token': str(access),
        'refresh_token': str(refresh),
        'user': user_serializer
    }

    return response

class ListUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = UserModel.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class BienesListView(APIView):
    queue = BienesModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = BienesSerializer(self.queue, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BienesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class BienesDetailView(APIView):
    queryset = BienesModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        bienes = self.queryset.get(pk=pk)
        serializer = BienesSerializer(bienes)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        bienes = self.queryset.get(pk=pk)
        serializer = BienesSerializer(bienes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bienes = self.queryset.get(pk=pk)
        bienes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import authenticate

from rest_framework import response, status


# Create your views here.

class RegisterAPIView(GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user=authenticate(username=email, password=password)

        if user:
            serializer=self.serializer_class(user)

            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'message':'Invalid Credintials, Try again!'}, status=status.HTTP_401_UNAUTHORIZED)
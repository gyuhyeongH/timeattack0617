from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import UserLog, User, UserType
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password


class SignUpView(APIView):
    def post(self, request):
        user_type = request.data.get('user_type', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        usertype = UserType.objects.get(user_type = user_type)
        User(user_type=usertype, email=email, password=make_password(password)).save()

        return Response(status=status.HTTP_200_OK)


class UserAPIView(APIView):
    # 로그인
    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        user = authenticate(request, email=email, password=password)

        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."})

        login(request, user)
        model = UserLog.object.get(email=user.email)
        model.save()
        return Response({"message": "login success!!"})

    def delete(self, request):
        logout(request)
        return Response({"message": "logout success!!"})


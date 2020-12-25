from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import update_last_login
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.settings import api_settings

from user.models import User
from user.serializers import AccountLoginSerializer, AccountRegisterSerializer

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class AccountLoginAPIView(CreateAPIView):
    permission_classes = permissions.AllowAny,
    serializer_class = AccountLoginSerializer

    @swagger_auto_schema(operation_summary="User log in api.")
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            try:
                user = User.objects.get(email=email)
                authenticate_user = authenticate(email=user.email, password=password)
                payload = JWT_PAYLOAD_HANDLER(authenticate_user)
                jwt_token = JWT_ENCODE_HANDLER(payload)
                user.access_token = jwt_token
                user.save()
                update_last_login(None, authenticate_user)
                login(self.request, authenticate_user)
                response = {
                    "success": True,
                    "status": status.HTTP_200_OK,
                    "error": False,
                    "message": "Successfully logged in."
                }
            except:
                response = {
                    "success": False,
                    "status": status.HTTP_404_NOT_FOUND,
                    "error": True,
                    "message": "User can not be found."
                }
            return Response(response)
        else:
            response = {
                "success": False,
                "status": status.HTTP_400_BAD_REQUEST,
                "error": True,
                "message": "400 - Bad Request"
            }
        return Response(response)


class AccountRegisterAPIView(CreateAPIView):
    permission_classes = permissions.AllowAny,
    serializer_class = AccountRegisterSerializer

    @swagger_auto_schema(operation_summary="Registration a new account api.")
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            username = serializer.data.get("username")
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            first_name = serializer.data.get("first_name")
            last_name = serializer.data.get("last_name")
            new_user = User(is_active=True, is_superuser=False, is_staff=True)
            new_user.username = username
            new_user.email = email
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.set_password(password)
            new_user.save()
            response = {
                "success": True,
                "status": status.HTTP_200_OK,
                "error": False,
                "message": "New user successfully created."
            }
            return Response(response)
        else:
            response = {
                "success": False,
                "status": status.HTTP_400_BAD_REQUEST,
                "error": True,
                "message": "400 - Bad Request"
            }
        return Response(response)


class AccountLogoutAPIView(CreateAPIView):
    permission_classes = permissions.IsAuthenticated,

    @swagger_auto_schema(operation_summary="If requested user is authenticated then log out.")
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = User.objects.get(email=request.user.email)
            user.access_token = None
            user.save()
            logout(request)
            response = {
                "success": True,
                "status": status.HTTP_200_OK,
                "error": False,
                "message": "Successfully logged out."
            }
            return Response(response)

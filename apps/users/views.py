from random import randint as rand

from django.contrib.auth.decorators import login_required
from rest_framework import status,generics
from .utils import Util
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
from django.shortcuts import redirect
from django.http import HttpResponsePermanentRedirect
import os
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from apps.users.serializers import  UserSerializer



@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def registration_view(request):
    data = {}
    first_name = request.data.get('first_name', "")
    last_name = request.data.get('last_name', "")
    email = request.data.get('email', None)
    password = request.data.get('password', None)
    password2 = request.data.get('password2', None)

    if not email:
        data['error_message'] = 'Email is required'
        data['response'] = 'Error'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email) or User.objects.filter(username=email):
        data['error_message'] = 'That email is already in use.'
        data['response'] = 'Error'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    if not password or password != password2:
        data['error_message'] = "Password didn't match"
        data['response'] = 'Error'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(
        email=email,
        username=email,
        first_name=first_name,
        last_name=last_name
    )
    user.set_password(password)
    user.save()

    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def logout(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@login_required
@permission_classes([IsAuthenticated])
def detail_user(request):
    user = request.user
    if user.is_anonymous:
        return Response('You need to log in', status=status.HTTP_401_UNAUTHORIZED)
    data = UserSerializer(user).data
    return Response(data, status=status.HTTP_200_OK)








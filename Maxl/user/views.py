from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.serializers import UserSerializer

from services.onboarding_service import create_user_and_wallet


# Create your views here.
@api_view(['POST'])
def create_wallet_account(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    create_user_and_wallet(serializer.validated_data)
    return Response({"message":"Registration successful"}, status=status.HTTP_201_CREATED)

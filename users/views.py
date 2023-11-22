from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core.validators import validate_email
from rest_framework.response import Response
from users.models import UserProfile
from rest_framework import status


# Create your views here.
@api_view(['POST'])
def register(request):
    username = request.data['username']
    email = request.data['email']
    try:
        validate_email(email)
    except:
        return Response({"message": "Enter a valid email address."})
    try:
        UserProfile.objects.create(username=username,email=email)
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


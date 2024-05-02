from django.shortcuts import render
from django.http import JsonResponse
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET' , 'POST'])
def profiles(request, format=None):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


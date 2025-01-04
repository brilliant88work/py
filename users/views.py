from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class UsersView(APIView):
    def get(self, request):
        return Response({'message': 'Hello from the USERs Microservice!'})
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . serializer import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class RegisterAPIView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(
                {"message":"User Registed successfully"},
                status=status.HTTP_201_CREATED
            )
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        return Response(
            {"name":request.user.first_name,
             "username":request.user.username}
        )
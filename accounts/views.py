from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics,status
from rest_framework.response import Response
from accounts.models import Account
from accounts.serializers import RegistrationSerializer, UsersSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
import requests

class CreateAccount(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        user_serializer = RegistrationSerializer(data=request.data)
        if user_serializer.is_valid():
            new_user = user_serializer.save()
            if new_user:
                resp=requests.post('http://127.0.0.1:8000/api-auth/token', data = {
                   'username':new_user.email,
                   'password':request.data['password'],
                #    'client_id':'Your Client ID', # This is for via social login 
                #    'client_secret':'Your Client Secret', # login after signup
                   'grant_type':'password'
               })
                return Response(resp.json(),status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class AllUsers(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Account.objects.all()
    serializer_class = UsersSerializer

class CurrentUser(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        serializer = UsersSerializer(self.request.user)
        return Response(serializer.data)

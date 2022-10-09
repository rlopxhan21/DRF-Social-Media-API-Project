from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegistrationSerializer
from django.contrib.auth.models import User



class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            useraccount = serializer.create()
            
            refresh = RefreshToken.for_user(useraccount)
            
            tokendata = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            
            return tokendata
        else:
            return serializer.erorrs
        

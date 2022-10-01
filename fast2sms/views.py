from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import *
import random
from .service import *
from rest_framework.views import APIView


def randomOTP(mobile):
    if mobile:
        OTP = random.randint(111,9999)
       
        return OTP  
    else:
        return False
    


class OtpViewSet(APIView):
    def post(self, request, *args, **kwargs):
        """
        A simple ViewSet for listing or retrieving users.
        """
        mobile=request.data.get('mobile')
        OTP = randomOTP(mobile)
        if OTP:
            is_mobile = Address.objects.filter(mobile=mobile)
            if is_mobile.exists():
                is_mobile = is_mobile.first()
                otp = is_mobile.otp
                if otp:
                    is_mobile.otp = str(OTP)
                    is_mobile.save()
                else:
                    pass
                count = is_mobile.count
                if count > 10:
                    return Response({'status': False, 'detail': 'Sender otp error exceed! Please contact customer support'})
                is_mobile.count += 1
                is_mobile.save()
                userauthsend(mobile,OTP)
                return Response({'status': True, 'detail': 'Otp sent successfully'}, status = status.HTTP_200_OK)
            else:
                Address.objects.create(mobile=mobile, otp=OTP)
                return Response({'status': True, 'detail': 'Otp sent successfully'}, status = status.HTTP_201_CREATED)
        else:
            return Response({'status': False, 'detail': 'Something went wrong'}, status = status.HTTP_400_BAD_REQUEST)
                    
                
        
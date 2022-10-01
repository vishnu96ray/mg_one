from django.urls import path

from .views import *

urlpatterns = [
    path('otp/', OtpViewSet.as_view(), name='opt'),
    


]

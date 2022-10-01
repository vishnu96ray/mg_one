
import requests
import json
import datetime
# from twilio.rest import Client




test = "https://www.fast2sms.com/dev/bulkV2"
api_key='OHKMb64QLimqUzFkagGXcErhSu8Dxp3lT2eNoYBtnVdRjIyZA7BUvLPobEcpOGnS4659mf1Fxq3ZhCrM'
# message='Welcome,\nYour username:'+str(username)+'\npassword:'+str(password)+'\nvisit:https://www/sabzicart.in',
# mobile_number = 7973706779

def userauthsend(mobile,otp):
    querystring = {"authorization":api_key,"sender_id":"TXTIND","message":'This ie Your OTP '+str(otp)+'',"route":"v3","numbers":mobile}
    headers = {
    'cache-control': "no-cache"
    }
    response = requests.request("GET", test, headers=headers, params=querystring)
    print(response)
    return(response)
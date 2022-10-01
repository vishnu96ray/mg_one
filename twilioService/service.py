import os
import random

from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def sendMessage():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                         from_='+15017122661',
                         to='+15558675310'
                     )

    print(message.sid)

def sendOTP():
    otp = random.randint(1000,9999)
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body=f"Your OTP is {otp}",
                         from_='+15017122661',
                         to='+15558675310'
                     )
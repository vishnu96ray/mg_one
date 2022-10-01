from rest_framework.response import Response
from rest_framework.decorators import api_view
import razorpay
client = razorpay.Client(auth=("<key_id>", "<key_secret>"))

# Create your views here.
@api_view(['POST'])
def createOrder(request):
    data = request.data
    amount = int(float(data['amount']))
    data = {"amount": amount, "currency": "INR"}
    payment = client.order.create(data=data)
    return Response({'order_id': payment['id'], 'amount': payment['amount'], 'currency': payment['currency']})


@api_view(['POST'])
def verifySignature(request):
    res = request.data

    params_dict = {
        'razorpay_payment_id': res['razorpay_paymentId'],
        'razorpay_order_id': res['razorpay_orderId'],
        'razorpay_signature': res['razorpay_signature']
    }
    res = client.utility.verify_payment_signature(params_dict)
    if res == True:
        return Response({'status': 'Payment Successful'})
    return Response({'status': 'Payment Failed'})

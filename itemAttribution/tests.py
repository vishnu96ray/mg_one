from rest_framework.response import Response
from .models import *


def findItemById(request):
    itemId = request.GET.get("item_id")
    product = ProductProduct.objects.filter(id=itemId)
    return Response({'item': product})



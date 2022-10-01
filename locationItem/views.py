from rest_framework.decorators import api_view
from rest_framework.response import Response

from locationItem.models import LocationItem


@api_view(['GET'])
def findItemByLocationHierarchy(request):
    location_hierarchy_id = request.GET.get("locationId")
    product = LocationItem.objects.filter(location_hierarchy_id=location_hierarchy_id)
    return Response({'item': product})

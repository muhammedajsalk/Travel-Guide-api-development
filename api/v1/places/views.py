from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.v1.places.serializers import PlaceSerializer,PlaceDetailsSerializer
from places.models import Place


@api_view(["GET"])
def places(request):
    instances = Place.objects.filter(is_deleted=False)
   
    context = {
        "request":request
    }
    
    serializer = PlaceSerializer(instances,many=True,context=context)
    response_data = {
        "status_code" : 6000,
        "data" : serializer.data
    }

    return Response(response_data)


@api_view(["GET"])
def place(request,pk):
    if Place.objects.filter(pk=pk).exists():
        instances = Place.objects.get(pk=pk)
    
        context = {
            "request":request
        }
        
        serializer = PlaceDetailsSerializer(instances,context=context)
        response_data = {
            "status_code" : 6000,
            "data" : serializer.data
        }

        return Response(response_data)
    else:
        response_data = {
            "status_code" : 6001,
            "data" : "Place not exist"
        }

        return Response(response_data)
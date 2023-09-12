from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny

from api.v1.places.serializers import PlaceSerializer,PlaceDetailsSerializer
from places.models import Place


@api_view(["GET"])
@permission_classes([AllowAny])
def places(request):
    instances = Place.objects.filter(is_deleted=False)
   
    q = (request.GET.get("q"))
    if q:
        instances = instances.filter(name__istartswith=q)

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
@permission_classes([AllowAny])
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
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected(request,pk):
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
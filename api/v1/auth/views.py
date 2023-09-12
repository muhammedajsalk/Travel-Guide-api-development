import requests
import json

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny

from django.contrib.auth.models import User


@api_view(["POST"])
@permission_classes([AllowAny])
def create(request):

    email = request.data['email']
    password = request.data['password']
    name = request.data['name']

    print('email',email)
    print('password',password)
    print('name',name)

    if not User.objects.filter(username=email).exists():
        
        User.objects.create_user(
            username = email,
            password = password,
            first_name = name
        )

        headers = {
            "Content-Type" : "application/json"
        }

        #data = f'"username": "{email}","password": "{password}"'
        #final_data = "{" + data + "}"

        data = {
            "username" : email,
            "password" : password,
        }

        protocol = "http://"
        if request.is_secure():
            protocol = "https://"
        
        host = request.get_host()

        url = protocol + host + "/api/v1/auth/token/"
       
        response = requests.post(url,headers=headers,data=json.dumps(data))

        if response.status_code == 200:

            response_data = {
                "status_code" : 6000,
                "data" : response.json(),
                "message" : "Account created"
            }
        else:
            response_data = {
                "status_code" : 6001,
                "data" : "An error occurred"
            }

    else:
         response_data = {
            "status_code" : 6001,
            "data" : "this account already exists"
        }

    return Response(response_data)
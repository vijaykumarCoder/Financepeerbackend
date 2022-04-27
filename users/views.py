from copyreg import constructor
from distutils import errors
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
import json

from .models import TestMode
from .serializers import RegisterSerializer,TestSerializer, UploadtSerializer
import pandas as pd


@api_view(['POST'])
def UploadJSON(request,*args,**kwargs):
    # print(type(request.body))
    try:
        serializer=UploadtSerializer(data=request.data,context={"request":request})
        serializer.is_valid()
        serializer.save()
        user = serializer.save()
        # print(user)       
        filepath = 'media/'+str(user)
        with open(filepath,'r') as persondata:
            emp = json.load(persondata)
        for i in emp:
            serializer = TestSerializer(data=i)
            # print(serializer)
            serializer.is_valid()
            serializer.save()
        dict_response={"error":False,"message":"Customer Request Data Save Successfully"}
        # else:
        #     print(serializer.errors)
    except Exception as e:
        print(e)
        dict_response={"error":True,"message":"Error During Saving Customer Request Data"}
    return Response(dict_response)
   
@api_view(['GET'])
def AllUsers(request):
    try:
        queryset = TestMode.objects.all()
        s = TestSerializer(queryset,many=True)
        res = s.data
    except TypeError:
       raise Http404("Poll does not exist")
    return Response(res) 

def serialize_user(user):
    return {
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    }

@api_view(['POST'])
def login(request):
    # print("hi",json.loads(request.body))
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return Response({
        'user_data': serialize_user(user),
        'token': token
    })

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user_info": serialize_user(user),
            "token": token
        })
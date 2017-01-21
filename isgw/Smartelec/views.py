from django.shortcuts import render
from django.http import HttpResponse
from Smartelec.models import Device,User,UserTransaction
import json


# Create your views here.

def deviceInfo(request):
	deviceId=request.GET.get("deviceId")

	return HttpResponse("We will be up shortly...!")

def userInfo(request):
	username=request.GET.get("name")
	user_object=User.objects.filter(name=username).values()
	print user_object
	output=json.dumps(user_object[0],indent=4)
	return HttpResponse(output,content_type="application/json")



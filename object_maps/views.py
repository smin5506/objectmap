from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import HBT
import urllib.request
import pandas
# Create your views here.

def hello(request):
	return render(request, 'test/setobstacle.html', {})

def setobstacle(request):
	if request.method == 'POST':		
		myID = request.POST['ID']
		myLocation = request.POST['Location']
		HBT.Head(ID=myID, Location = myLocation).save()
		
		myType = request.POST['Type']
		myDataSequence = request.POST['DataSequence']
		HBT.Body(Type=myType, DataSequence=myDataSequence).save()
		
		myResult = request.POST['Result']
		myAccuracy = request.POST['Accuracy']
		HBT.Tail(Result=myResult, Accuracy=myAccuracy).save()
	return HttpResponse("good")
			
def viewobstacle(request):
	Head_data = serializers.serialize('json', HBT.Head.objects.all())
	Body_data = serializers.serialize('json', HBT.Body.objects.all())
	Tail_data = serializers.serialize('json', HBT.Tail.objects.all())
	data = Head_data + Body_data + Tail_data
	return HttpResponse(data, content_type='json')
	

	
	
	
	

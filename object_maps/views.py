from django.shortcuts import render
from django.http import HttpResponse
from object_maps.models import objects

# Create your views here.
def hello(request):
	return HttpResponse("hello, world!")
	
def Insertobject(request, id, objectX, objectY, width, height):
	objects(id=id, objectX=objectX, objectY=objectY, width=width, height=height).save()
	#return render(request, 'object_maps/mypage.html',{'welcome_text': 'Insert: ' + id})
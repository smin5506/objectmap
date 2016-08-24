from django.shortcuts import render
from django.http import HttpResponse
from object_maps.models import objects

# Create your views here.
def hello(request):
	return HttpResponse("hello, world!")
	
def Insertobject(request, id, objectX, objectY, width, height):
	objects(id=id, objectX=objectX, objectY=objectY, width=width, height=height).save()
	#return render(request, 'object_maps/mypage.html',{'welcome_text': 'Insert: ' + id})
	return HttpResponse("Success! id: %s" %id)
	
def viewobject(request):
	for row in objects.objects.all():
		id = str(row.id)
		objectX = str(row.objectX)
		objectY = str(row.objectY)
		width = str(row.width)
		height = str(row.height)
		
		data = "id: " + id + ", objectX: " + objectX + ", objectY: " + objectY + ", width: " + width + ", height: " + height
		return HttpResponse(data)
	return HttpResponse("end")
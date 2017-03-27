from object_maps.models import HBT

def search_def():
	print("ID, Time, Location, Type, DataSequence, Result, Accuracy")
	search = input("search data: ")
	
	if(search == "ID") :
		mid = input("search data: ")
		data = HBT.Head.objects.filter(id=mid)

	elif(search == "Time") :
		mtime = input("search data(y-m-d, y-m-d): ")
		mtime1, mtime2 = mtime.split(",")
		data = HBT.Head.objects.filter(Time__range=[mtime1, mtime2])

	elif(search == "Location") :
		mlocation = input("search data(lon, lat): ")
		data = HBT.Head.objects.filter(Location=mlocation)
		
	elif(search == "Type") :
		mtype = input("search data: ")
		data = HBT.Body.objects.filter(Type=mtype)
		
	elif(search == "DataSequence") :
		pass
		#HBT.Head.objects.get(jsonfield_contains={'username':username})
		#dataframe형태로 변경하는 코드 작성
		
	elif(search == "Result") :
		mresult= input("search data: ")
		data = HBT.Body.objects.filter(Result=mresult)
		
	elif(search == "Accuraccy") :
		maccuraccy= input("search data: ")
		data = HBT.Body.objects.filter(Accuraccy=maccuraccy)
		pass
		
	else:
		print("실패")
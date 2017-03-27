from object_maps.models import HBT

def save_def():
	type = input("type: ")
	if(type == "head") :
		print("ID, Time, Location")
		myID = input("ID: ")
		myTime = input("Time: ")
		myLocation = input("Location: ")
		HBT.Head(ID=myID, Time=myTime, Location = myLocation).save()
		
	elif(type == "body") :
		print("Type, DataSequence")
		myType = input("Type: ")
		myDataSequence = input("DataSequence: ")
		HBT.Body(Type=myType, DataSequence=myDataSequence).save()
		
	elif(type == "tail") :
		print("Result, Accuracy")
		myResult = input("Result: ")
		myAccuracy = input("Accuracy: ")
		HBT.Tail(Result=myResult, Accuracy=myAccuracy).save()
		
	else:
		print("실패")
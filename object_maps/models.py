from django.db import models
from location_field.models.plain import PlainLocationField
import pandas as pd
from django_pgjsonb import JSONField

# Create your models here.
class HBT(models.Model):
	class Head(models.Model):
		ID = models.IntegerField(null=True)
		Time = models.DateTimeField(auto_now = True)
		Location = PlainLocationField(based_fields=['city'], zoom=7)
		#objects = models.GeoManager()

		
	class Body(models.Model):
		Type = models.CharField(max_length=20)
		DataSequence = JSONField()
		
		def store_dataframe(self, dataframe):
			self.dfjson = dataframe.to_json()

		def load_dataframe(self):
				return pandas.read_json(self.json)
				
	class Tail(models.Model):
		Result = models.TextField()
		Accuracy = models.FloatField()
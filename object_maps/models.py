from django.db import models

# Create your models here.
class objects(models.Model):
	id = models.IntegerField(primary_key=True)
	objectX = models.FloatField(null=True)
	objectY = models.FloatField(null=True)
	width = models.IntegerField(null=True)
	height = models.IntegerField(null=True)
	
	'''
	def __str__(self):
		return self.id
	'''
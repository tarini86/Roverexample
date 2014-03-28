from django.db import models

# Create your models here.

class Person(models.Model):
	personName_text = models.CharField(max_length=100)
	personAge 		= models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.personName_text
		
	class Meta:
		ordering = ['personName_text']
	
class Dog(models.Model):
	personName 	= models.ForeignKey(Person)
	dogName 	= models.CharField(max_length=50)
	age			= models.IntegerField(default=0)
	breed		= models.CharField(max_length=100)
	nature		= models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.dogName
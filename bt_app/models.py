from django.db import models

# Create your models here.
class  Object(models.Model):
	point_id = models.IntegerField(verbose_name="Point_ID")
	location = models.TextField(max_length=100, verbose_name="Location")
	ip_address = models.TextField(max_length=128, verbose_name="IP_address")

class Object_Info(models.Model):
	point = models.ForeignKey(Object)	
	type = models.TextField(max_length=100, verbose_name="Type")
	node_id = models.IntegerField(verbose_name="Location")
	notes = models.TextField(max_length=100, verbose_name="Notes")


		
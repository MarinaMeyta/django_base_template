from django.db import models

# Create your models here.
class  Person(models.Model):
	name = models.TextField(max_length=100, verbose_name="Name")
	surname = models.TextField(max_length=100, verbose_name="Surname")
		
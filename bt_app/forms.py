from django import forms
from .models import Object
from .models import Object_Info

class ObjectForm(forms.ModelForm):
	class Meta:
		model = Object
		fields = ("point_id", "location", "ip_address")

	def clean(self):
		cd = self.cleaned_data

class ObjectInfoForm(forms.ModelForm):
	class Meta:
		model = Object_Info
		fields = ("point", "type", "node_id", "notes")

	def clean(self):
		cd = self.cleaned_data

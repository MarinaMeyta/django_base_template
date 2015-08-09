from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ("name", "surname",)

	def clean(self):
		cd = self.cleaned_data

	# def clean_name(self):
	# 	cd = self.cleaned_data

	# 	name = cd.get('name')

	# 	if len(name) < 3:
	# 		raise forms.ValidationError("Please, write more than two chars") 

	# 	return name

	# def clean_surname(self):
	# 	cd = self.cleaned_data

	# 	surname = cd.get('surname')

	# 	if len(surname) < 3:
	# 		raise forms.ValidationError("Please, write more than two chars") 

	# 	return surname

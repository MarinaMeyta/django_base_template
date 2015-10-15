import django_tables2 as tables
from bt_app.models import Person

class PersonTable(tables.Table):
	class Meta:
		model = Person
		attrs = {"class": "table"}
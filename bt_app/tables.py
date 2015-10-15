import django_tables2 as tables
from bt_app.models import Object
from bt_app.models import Object_Info

class ObjectTable(tables.Table):
	class Meta:
		model = Object
		attrs = {"class": "table"}

class ObjectInfoTable(tables.Table):
	class Meta:
		model = Object_Info
		attrs = {"class": "table"}
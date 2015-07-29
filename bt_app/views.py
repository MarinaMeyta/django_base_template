from django.shortcuts import render
from bt_app.models import Person
from django_tables2 import RequestConfig
from bt_app.tables import PersonTable

# Create your views here.
def home_page(request):
    return render(request, 'base_index.html', {})

def people_page(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'base_people.html', {'table': table})

def about_page(request):
    return render(request, 'base_about.html', {})

def contacts_page(request):
    return render(request, 'base_contacts.html', {})





def add_person(request):
	if request.method == "POST":
		person = request.POST['new_person']
	else:
		person = ''

    
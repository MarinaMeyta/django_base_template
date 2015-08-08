from django.shortcuts import render
from bt_app.models import Person
from django_tables2 import RequestConfig
from bt_app.tables import PersonTable
from django.core.context_processors import csrf
from bt_app.forms import PersonForm
# for parsing serialized query string
from urllib.parse import parse_qs

from django.core import serializers

from django.http import HttpResponse

from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render


from django.template import RequestContext

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

        query = request.POST['serialized_data']
        form_data = parse_qs(query)
        print (form_data)

        form_data_clean = {'name': form_data['Name'][0], 'surname': form_data['Surname'][0]}
        print (form_data_clean)

        new_person_form = PersonForm(form_data_clean)
        print (new_person_form)      

        if new_person_form.is_valid():
            new_person_form.clean()
            print ('ok')

            new_person = Person()
            new_person.name = new_person_form.cleaned_data['name']
            new_person.surname = new_person_form.cleaned_data['surname']
            new_person.save()

            print (new_person.name)
            print (new_person.surname)

            return redirect('base_people.html', {'table': table})






    #         # new_person_form.save()
    #         print ('ok')
    #         print (new_person_form)

    #         name = new_person_form.cleaned_data['name']
    #         surname = new_person_form.cleaned_data['surname']
    #         # id = ?????

    #         # html = render('base_people.html', {'table': table}, context_instance=RequestContext(request))
    #         return render('base_people.html', {'table': table}, c)
    #         #return render_to_response('base_people.html', {'table': table})
    #     else:
    #         print ('validation error')
    # # else:
    # #     person = ''

    # #return render('base_people.html', c)

    
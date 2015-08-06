from django.shortcuts import render
from bt_app.models import Person
from django_tables2 import RequestConfig
from bt_app.tables import PersonTable
from django.core.context_processors import csrf

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
    print ('request: ', request)

    #c = {}
    #c.update(csrf(request))

    if request.method == "POST":
        # person = request.POST['new_person']
        new_person_form = PersonForm(request.POST)
        if new_person_form.is_valid():
            new_person_form.save()
            # html = render('base_people.html', {'table': table}, context_instance=RequestContext(request))
            return render('base_people.html', {'table': table}, c)
            #return render_to_response('base_people.html', {'table': table})
    # else:
    #     person = ''

    #return render('base_people.html', c)

    
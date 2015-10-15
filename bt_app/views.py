
from django.shortcuts import render
from django_tables2 import RequestConfig

from django.core.context_processors import csrf

# for parsing serialized query string
from urlparse import urlparse
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render

from django.template import RequestContext


from bt_app.models import Object, Object_Info
from bt_app.tables import ObjectTable, ObjectInfoTable
from bt_app.forms import ObjectForm, ObjectInfoForm




# Create your views here.
def home_page(request):
    return render(request, 'home.html', {})

def objects_page(request):
    table = ObjectTable(Object.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'objects.html', {'table': table})

def about_page(request):
    return render(request, 'about.html', {})





def add_object(request):

    if request.method == "POST":

        query = request.POST['serialized_data']
        form_data = urlarse.parse_qs(query)
        print form_data

        form_data_clean = {'point_id': form_data['Point_ID'][0], 'location': form_data['Location'][0], 'ip_address': form_data['IP_address'][0]}
        print form_data_clean

        new_object_form = ObjectForm(form_data_clean)
        print new_object_form

        if new_object_form.is_valid():
            new_object_form.clean()
            print 'ok'

            new_object = Object()
            new_object.point_id = new_object_form.cleaned_data['point_id']
            new_object.location = new_object_form.cleaned_data['location']
            new_object.ip_address = new_object_form.cleaned_data['ip_address']
            new_object.save()

            return HttpResponseRedirect(request, 'objects.html', {'table': table})

from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'base_index.html', {})

def about_page(request):
   	return render(request, 'base_about.html', {})

def contacts_page(request):
   	return render(request, 'base_contacts.html', {})
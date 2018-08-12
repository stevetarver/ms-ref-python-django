from django.shortcuts import render
from django.http import HttpResponse
from .models import Contacts

# Create your views here.
def index(request):

    contacts = Contacts.objects.all()
    context = {
        'title': 'Contact List',
        'contacts': contacts,
    }
    return render(request, 'contacts/index.html', context=context)

def details(request, id):
    contact = Contacts.objects.get(id=id)
    context = {
        'title': 'Contact Details',
        'contact': contact,
    }
    return render(request, 'contacts/details.html', context=context)

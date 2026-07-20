from django.shortcuts import render
from django.http import HttpResponse
from .models import contact_message
from templates.form import

def home_page_view (request):
    context ={
        'nom': 'Gedeon',
        'age': '25',
        'couleurs':[ 'gray','green','pink']
    }
    return render(request,'home.html',context)

def contact_page_view (request):
    succes=None
    if request.methode == 'POST':
        form =
    else
    return render (request,'contact.html')
# Create your views here.
def message_list_view(request):
    donnes= contact_message.objects.all()
    context={"donnes":donnes}
    return render(request,'message_list.html',context)
    

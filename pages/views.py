from django.shortcuts import render
from django.http import HttpResponse
from .models import contact_message

def home_page_view (request):
    context ={
        'nom': 'Gedeon',
        'age': '25',
        'couleurs':[ 'gray','green','pink']
    }
    return render(request,'home.html',context)

def contact_page_view (request):
    return render (request,'contact.html')
# Create your views here.
def message_list_view(request):
    re= contact_message.objects.all()
    context={"messages_list":re}
    return render(request,'message_list.html',context)
    

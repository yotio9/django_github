from django.shortcuts import render
from django.http import HttpResponse

def home_page_view (request):
    context ={
        'nom': 'Gedeon',
        'age': '25',
        'couleurs':[ 'gray','green','pink']
    }
    return render(request,'home.html',context)

def contact_page_view (request):
    return render (request)
# Create your views here.

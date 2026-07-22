from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import contact_message
from templates.form import contact_message_Form,UsersForm
from django.contrib.auth import authenticate, login

def home_page_view (request):
   erreur=None
   succes=None
   if request.method == 'POST':
   #je stocke les donnees dans un variable
    form= UsersForm(request.POST)
    if form.is_valid():
       
      #je recupere les elements dont jai besoin dans des varialbles
      email=form.cleaned_data.get('email')
      mot_de_passe=form.cleaned_data.get('mot_de_passe')
      #django verifier maitenant si les donnees existe das la base de donnees
      user=authenticate(request,username=email,password=mot_de_passe)
      if user is not None:
         #on donne acces a une page
         login(request,user)
         return redirect ("bienvenue.html")

   return render(request,'home.html')

def bienvenue_views(request):
   return render (request,'bienvenue.html')




def contact_page_view (request):
    succes=None
    if request.method == 'POST':
        form = contact_message_Form(request.POST)
        if form.is_valid():
            form.save()
            succes="votre message a bien ete envoyer"
    else:
        contact_message_Form()
        context={ 
            'form': form,
            'succes': succes
        }
    return render (request,'contact.html',context)
# Create your views here.



def message_list_view(request):
    donnes= contact_message.objects.all()
    context={"donnes":donnes}
    return render(request,'message_list.html',context)
    

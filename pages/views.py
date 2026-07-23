from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import contact_message,Users,Grades,Students,Subjects,Teachers,Absences
from templates.form import contact_message_Form,UsersForm, StudentsForm,SubjectsForm,AbsenceForm,TeacherForm,GradeForm
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
    
def inscrption_send(request):
    if request.method == 'POST':
       valeur_name=request.POST.get('name')
       valeur_email=request.POST.get('email')
       valeur_mdp=request.POST.get('mot_de_passe')
       valeur_role=request.POST.get('role')
       Users.objects.create(
          name=valeur_name,
          email=valeur_email,
          mot_de_passe=valeur_mdp,
          role=valeur_role
       )
       return redirect('/')
    return render(request,'inscription.html')

      
   
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import contact_message,Users,Grades,Students,Subjects,Teachers,Absences,Classes
from templates.form import contact_message_Form,UsersForm, StudentsForm,SubjectsForm,AbsenceForm,TeacherForm,GradeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from compte.views import connexion_view


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
       age=request.POST.get('age')
       classe=request.POST.get('classe')
       name=request.POST.get('name')
       email=request.POST.get('email')
       mdp=request.POST.get('mot_de_passe')
       role=request.POST.get('role')
       matiere=request.POST.get('matiere')
       prenom=request.POST.get('prenom')
       authenticate.objects.create(
          name=name,
          email=email,
          mot_de_passe=mdp,
          role=role
       )

       if prenom or classe:
          Students.objects.create(
             nom=name,
             prenom=prenom,
             classe=classe,
             age=age
          )
       elif matiere:
          Subjects.objects.create(
             nom=matiere
          )
            
       return redirect('/')
    return render(request,'inscription.html')

def choix_users(request):
   return render(request,'choix_users.html')


############################################################""

def inscrption_etd(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        prenom = request.POST.get('prenom')
        classe = request.POST.get('classe')
        age = request.POST.get('age')

        email = request.POST.get('email')
        mdp = request.POST.get('mot_de_passe')
        role = "etudiant"
        
        classe_obj, created = Classes.objects.get_or_create(name=classe)
        
        stuud = Users.objects.create_user(
            username=name,
            email=email,
            password=mdp,
            role=role,
        )
  
        # CORRECTION ICI : Utilisez 'user' au lieu de 'user_id'
        Students.objects.create(
            user=stuud,
            nom=name,
            prenom=prenom,
            age=age,
            classe=classe_obj,# <-- Changement effectué ici
        )
        print(stuud)
        return redirect('/')
    return render(request, 'inscription_etd.html')


def choix_users(request):
   return render(request,'choix_users.html')

@login_required  # Force l'utilisateur à se connecter avant de voir la page
def espace_etd(request):
    utilisateur_connect= request.user
    # Récupère UNIQUEMENT l'étudiant connecté avec ses relations chargées
    try:
        donnees = Students.objects.select_related('user', 'classe').get(user=request.user)
    except Students.DoesNotExist:
        donnees = None  # Évite un crash si un admin connecté n'est pas un étudiant
    utilisateur_connect= request.user
    return render(request, 'espace_etd.html', {"donnees": donnees})

#######################################
def inscrption_prf(request):
    if request.method == 'POST':
  
       name=request.POST.get('name')
       email=request.POST.get('email')
       mdp=request.POST.get("mot_de_passe")
       role="professeur"
       matiere=request.POST.get('matiere')
      
       teach=Users.objects.create_user(
          username=name,
          email=email,
          password=mdp,
          role=role
       )

       Teachers.objects.create(
                 user=teach,
                 matiere=matiere,
                 
              )

            
       return redirect('/')
    return render(request,'inscription_prf.html')

def choix_users(request):
   return render(request,'choix_users.html')

@login_required  # Force l'utilisateur à se connecter avant de voir la page
def espace_prf(request):
    # Récupère UNIQUEMENT l'étudiant connecté avec ses relations chargées
      try:
         donnees = Teachers.objects.select_related('user').get(user=request.user)
         stud=Students.objects.select_related('classe')
         sub=Subjects.objects.all()
         
      except Teachers.DoesNotExist:
         donnees = None  # Évite un crash si un admin connecté n'est pas un professeur
         stud=[]
         sub=[]
      context={"donnees":donnees,"stud":stud,'sub':sub}

      if request.method=='POST':
         eleve=request.POST.get('student_id')
         note=request.POST.get('note')
         date=request.POST.get('date')
         status=request.POST.get('status')
         Grades.objects.create(
            note=note,
            

         )
      return render(request, 'espace_prf.html',context)




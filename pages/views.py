from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import contact_message,Users,Grades,Students,Subjects,Teachers,Absences,Classes
from templates.form import contact_message_Form,UsersForm, StudentsForm,SubjectsForm,AbsenceForm,TeacherForm,GradeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from compte.views import connexion_view
from django.contrib import messages


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
        abss= Absences.objects.filter(id_students=donnees)
        grd=Grades.objects.filter(id_students=donnees)
    except Students.DoesNotExist:
        donnees = None  # Évite un crash si un admin connecté n'est pas un étudiant
        abss=[]
        grd=[]
    utilisateur_connect= request.user
    return render(request, 'espace_etd.html', {"donnees": donnees,"abss":abss,"grd":grd})

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
         sub=Subjects.objects.filter(id_teachers=donnees)
         
      except Teachers.DoesNotExist:
         donnees = None  # Évite un crash si un admin connecté n'est pas un professeur
         stud=[]
         sub=[]
      context={"donnees":donnees,"stud":stud,'sub':sub}
     
      if request.method=='POST':
        
         print("-> UNE REQUETE POST A ETE REÇUE !") # S'affichera dans votre terminal
        
         if not donnees:
            context["error"] = "Action impossible : Vous êtes connecté mais vous n'êtes pas enregistré comme Professeur dans la base de données."
            return render(request, 'espace_prf.html', context)

         
         eleve=request.POST.get('student')
         eleve1=request.POST.get('student1')
         note=request.POST.get('note')
         date=request.POST.get('date')
         status=request.POST.get('status')
         matiere=request.POST.get('Matiere')
         form_type=request.POST.get('form_type')

         if form_type =='note':
                       try:
                                   vrai_eleve=Students.objects.get(id=eleve) #recupere l'id de, l' eleve dans le champ student
                                   vrai_matiere=Subjects.objects.get(id=matiere)
                                   Grades.objects.create(
                                               note=note,
                                               id_students=vrai_eleve,#id brut dans la colonnes id_student
                                               id_subjects=vrai_matiere
                                                 )
                                   print('NOTE ENREGISTRER')
                                   return redirect('espace_prf')

         
                       except Exception as e:
            
                         context["error"] = f"Erreur d'enregistrement : {e}"
                         return render(request, 'espace_prf.html', context)
         elif form_type =='absences':
             try:
                 vrai_eleve=Students.objects.get(id=eleve1)
                 Absences.objects.create(
                     id_students=vrai_eleve,
                     date=date,
                     status=status
                 )
                 print('ABSENCES ENREGISTRER')
                 return redirect('espace_prf')

             
             except Exception as e:
                         
                     context["error"] = f"Erreur d'enregistrement : {e}"
                     return render(request, 'espace_prf.html', context)    
                               
      return render(request, 'espace_prf.html',context)


@login_required
def modifier_prf(request):
    try:
        donnees = Teachers.objects.select_related('user').get(user=request.user)
        stud = Students.objects.select_related('classe')
        sub = Subjects.objects.filter(id_teachers=donnees)
        absences = Absences.objects.all()
        # Notes uniquement dans la matière du prof connecté
        grades = Grades.objects.filter(
            id_subjects__id_teachers=donnees
        ).select_related('id_students', 'id_subjects')
    except Teachers.DoesNotExist:
        donnees = None
        stud = []
        sub = []
        absences = []
        grades = []

    selected_student_id = request.GET.get('student_id')
    selected_subject_id = request.GET.get('subject_id')
    grd = []

    if selected_student_id and selected_subject_id:
        grd = Grades.objects.filter(
            id_students__id=selected_student_id,
            id_subjects__id=selected_subject_id,
            id_subjects__id_teachers=donnees  # sécurité : matière du prof uniquement
        ).select_related('id_students', 'id_subjects')
    elif selected_student_id:
        grd = Grades.objects.filter(
            id_students__id=selected_student_id,
            id_subjects__id_teachers=donnees  # sécurité : matière du prof uniquement
        ).select_related('id_students', 'id_subjects')

    if request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type == "modifier_note":
            grade_id = request.POST.get("grade_id")
            new_note = request.POST.get("note")
            post_student_id = request.POST.get("student_id")
            post_subject_id = request.POST.get("subject_id")
            grade = Grades.objects.get(id=grade_id)
            grade.note = new_note
            grade.save()
            return redirect(f"{request.path}?student_id={post_student_id}&subject_id={post_subject_id}")

    context = {
        "donnees": donnees,
        "stud": stud,
        "sub": sub,
        "absences": absences,
        "grades": grades,
        "grd": grd,
        "selected_student_id": selected_student_id,
        "selected_subject_id": selected_subject_id,
    }
    return render(request, "espace_prf_modif.html", context)


def admin_identify(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        pwd = request.POST.get('password')
        
     
        try:
            Users.objects.create_superuser(
                username=username,
                email=email,
                password=pwd
            )
            messages.success(request, "Superutilisateur créé !")
            # 2. Rediriger vers l'admin après le succès
            return redirect('admin_identify') 
        except Exception as e:
            messages.error(request, f"Erreur : {e}")

    return render(request, "admin_identify.html")


def admin_authen(request):
    if request.method == 'POST':
        # 1. Récupérer les données saisies par l'utilisateur
        nom_utilisateur = request.POST.get('username')
        mot_de_passe = request.POST.get('password')
        user = authenticate(request, username=nom_utilisateur, password=mot_de_passe)
    
        if user is not None:
            login(request, user)
            if hasattr(user,'role') and user.role=="":
                return redirect("admin_identify")
            
            else:
                context={"error":"accès refuser vous netes pas admin"}
                return render(request, 'admin_authen.html',context)
                        # Si la requête est en GET, on affiche juste la page avec le formulaire
        else:
            context={"error":" mot de passe ou nom utlisateur incorrect"}
            return render(request,'admin_authen.html',context)                
    return render(request,"admin_authen.html")

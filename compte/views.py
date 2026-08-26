from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Users

# Create your views here.
def connexion_view(request):
    if request.method == 'POST':
        # 1. Récupérer les données saisies par l'utilisateur
        nom_utilisateur = request.POST.get('username')
        mot_de_passe = request.POST.get('password')
        user = authenticate(request, username=nom_utilisateur, password=mot_de_passe)
    
        if user is not None:
            login(request, user)
            if hasattr(user,'role') and user.role=="etudiant":
                return redirect("espace_etd")
            elif hasattr(user,"role") and user.role == "professeur":
                return redirect("espace_prf")
            elif hasattr(user,'role')and user.role =="":
                return redirect("/admin/")
                
            else:
                context={ "error":" Nom utlisatuer ou Mot de passe incorrect "}
                return render(request, 'connection.html', context)


        else:
            # ---- CAS MANQUANT : identifiants invalides ----
            context = {"error": "Nom d'utilisateur ou mot de passe incorrect."}
            return render(request, 'connection.html', context)                # Si la requête est en GET, on affiche juste la page avec le formulaire
    return render(request,"connection.html")      
        
        


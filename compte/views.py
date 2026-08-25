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
                return render(request, 'connection.html', {'error': 'Identifiants ou mot de passe invalides.'})
                        # Si la requête est en GET, on affiche juste la page avec le formulaire
    return render(request,"connection.html")      # Si la requête est en GET, on affiche juste la page avec le formulaire
        
        


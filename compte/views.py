from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def connexion_view(request):
    if request.method == 'POST':
        # 1. Récupérer les données saisies par l'utilisateur
        nom_utilisateur = request.POST.get('username')
        mot_de_passe = request.POST.get('password')
        role = request.POST.get('role')  # Récupérer le rôle sélectionné par l'utilisateur
        if role =='etudiant':
            # 2. Vérifier si l'utilisateur existe avec ce mot de passe
                    user = authenticate(request, username=nom_utilisateur, password=mot_de_passe)
                    print(user)
                    if user is not None:
                        # 3. Connecter officiellement l'utilisateur (création de la session)
                        login(request, user)
                        return redirect('espace_etd')  # Redirige vers son espace
                    else:
                        # Identifiants incorrects
                        return render(request, 'connection.html', {'error': 'Identifiants invalides.'})
                        
        elif role =='professeur':  
                    # 2. Vérifier si l'utilisateur existe avec ce mot de passe
                            user = authenticate(request, username=nom_utilisateur, password=mot_de_passe)
                            print(user)
                            if user is not None:
                                # 3. Connecter officiellement l'utilisateur (création de la session)
                                login(request, user)
                                return redirect('espace_prf')  # Redirige vers son espace
                            else:
                                # Identifiants incorrects
                                return render(request, 'connection.html', {'error': 'Identifiants invalides.'})
                                
                        # Si la requête est en GET, on affiche juste la page avec le formulaire
        return render(request,"connection.html")      # Si la requête est en GET, on affiche juste la page avec le formulaire
        
        


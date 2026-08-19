from django.urls import path
from pages import views

urlpatterns=[
    path("", views.home_page_view),

    path("messages/",views.message_list_view),
    path("bienvenue/",views.bienvenue_views),
    path("inscription_prf/",views.inscrption_prf,name='inscription_prf'),
    path("inscription_etd/",views.inscrption_etd,name='inscription_etd'),
    path("choix_user/",views.choix_users,name='choix_users'),
    path('espace_etd/',views.espace_etd,name="espace_etd"),
    path('espace_prf/',views.espace_prf,name="espace_prf"),
    path('espace_prf_modif/',views.modifier_prf,name="modifier_prf")
    
    
    #path('espace_prf/',views,espace_prf,name="espace_prf")
]
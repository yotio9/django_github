from django.contrib import admin

from .models import contact_message,Students

# pour que ca s'enregistre dans le server                                   

class contact_message_admin(admin.ModelAdmin):
    list_display=(('name','email','created_at','is_treated'))# pour personnaliser l'affichage des donnees
    list_filter=('is_treated','created_at')# definer  filtre en fonction 2
    search_fields=('name','email')

admin.site.register(contact_message,contact_message_admin)
class StudentAdmin(admin.ModelAdmin):
    list_display=("nom","prenom",'age')
admin.site.register(Students,StudentAdmin)
from django import forms

from pages.models import Teachers, Grades ,Students,Subjects,Users,Absences,contact_message # On importe vos modèles ici

class contact_message_Form(forms.ModelForm):

    class Meta:
        model = contact_message       # 1. On dit à Django quel modèle utiliser
        fields = '__all__'  
   
   

# Formulaire pour le modèle Grade
class GradeForm(forms.ModelForm):# methode django pour creer des formulaire

    class Meta:
        model = Grades        # 1. On dit à Django quel modèle utiliser
        fields = '__all__'   # 2. On lui dit de prendre TOUS les champs du modèle 

# Formulaire pour le modèle Teacher (Professeur)
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = '__all__' # On peut aussi lister les champs un par un

class SubjectsForm(forms.ModelForm):
    class Meta:
        model= Subjects # Instruction 1 : "Construis ce formulaire à partir du modèle Grade
        fields='__all__'# contruis un des champs html pour ses colonnes

class UsersForm(forms.ModelForm):
    class Meta:
        model=Users
        fields='__all__'

class StudentsForm(forms.ModelForm):
    class Meta:
        model=Users
        fields='__all__'

class AbsenseForm(forms.ModelForm):
    class Meta:
        model=Users
        fields='__all__'
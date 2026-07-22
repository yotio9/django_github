from django.db import models

# Create your models here.
class contact_message(models.Model):
    name=models.CharField(max_length=100)
    email= models.EmailField()
    message= models.TextField()
    created_at=models.DateTimeField(
        auto_now_add=True
    )
    is_treated=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Users(models.Model):
   name=models.CharField(max_length=100)
   role=models.CharField(max_length=100)
   mot_de_passe=models.CharField(max_length=8)
   email=models.EmailField()

class Teachers(models.Model):
    nom=models.CharField(max_length=100)
    matiere=models.CharField(max_length=100)
    users_id=models.ForeignKey('Users',on_delete=models.CASCADE,related_name='teachers')

class Subjects(models.Model):
    nom=models.CharField(max_length=100)
    id_teachers=models.ForeignKey('Teachers',on_delete=models.CASCADE,related_name='subjects')

class Students(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    age=models.CharField(max_length=10)
    classe=models.CharField(max_length=100)
    users_id= models.ForeignKey('Users',on_delete=models.CASCADE,related_name='students')

class Grades (models.Model):
     id_students= models.ForeignKey('Students',on_delete=models.CASCADE,related_name='grades')
     id_subjects= models.ForeignKey('Subjects',on_delete=models.CASCADE,related_name='grades')
     age=models.CharField(max_length=10)

     
class Absences (models.Model):
     id_students= models.ForeignKey('Students',on_delete=models.CASCADE,related_name='absences')
     date=models.DateTimeField(auto_now_add=True)
     status=models.CharField(max_length=10)




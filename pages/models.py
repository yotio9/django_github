from django.db import models
from django.contrib.auth.models import  AbstractUser
from compte.models import Users

class Classes(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

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


  

class Teachers(models.Model):
    user=models.OneToOneField(Users,on_delete=models.CASCADE,related_name='teachers')
    matiere=models.CharField(max_length=100)
    def  __str__(self):
                 return f"{self.user}"
   
class Subjects(models.Model):
    nom=models.CharField(max_length=100)
    id_teachers=models.ForeignKey(Teachers,on_delete=models.SET_NULL,related_name='subjects',   null=True,
    blank=True)
    def  __str__(self):
                 return f"{self.nom}-{self.id_teachers}"

class Students(models.Model):
    user=models.OneToOneField(Users,on_delete=models.CASCADE,related_name='students' )
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    age=models.CharField(max_length=10)
    classe=models.ForeignKey(Classes,on_delete=models.SET_NULL,related_name='students', null=True,
    blank=True)
    def  __str__(self):
        return f"{self.nom}"
    

class Grades (models.Model):
     id_students= models.ForeignKey(Students,on_delete=models.CASCADE,related_name='grades',   null=True,
    blank=True)
     id_subjects= models.ForeignKey(Subjects,on_delete=models.CASCADE,related_name='grades',   null=True,
    blank=True)
     note=models.FloatField(default=0.0)
     def  __str__(self):
             return f"{self.note}-{self.id_students}"

     
class Absences (models.Model):
     id_students= models.ForeignKey(Students,on_delete=models.SET_NULL,related_name='absences',   null=True,
    blank=True)
     date=models.DateTimeField(auto_now_add=True)
     status=models.CharField(max_length=10)
     def  __str__(self):
                  return f"{self.date} {self.status} -{self.id_students}"





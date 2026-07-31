from django.urls import path
from .views import connexion_view


urlpatterns=[
  path("connection/",connexion_view,name='connection'),
 ]
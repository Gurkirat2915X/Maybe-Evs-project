from django.urls import path
from . import views

urlpatterns = [
     path("Home", views.index, name="index"),
     path("Causes",views.Causes,name="Causes")
 ]
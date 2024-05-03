from django.urls import path
from . import views

urlpatterns = [
     path("Home", views.index, name="index"),
     path("Causes",views.Causes,name="Causes"),
     path("Solutions",views.Solutions,name="Solution"),
     path("NGOs",views.NGOs,name="NGOs"),
     path("Forms",views.Forms,name="Forms")
 ]
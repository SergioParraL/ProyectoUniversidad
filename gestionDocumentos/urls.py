"""UEBJuan_Ignacio_Montilla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
 
    path('Docs/', views.Register_Docs, name="Docs"),
    path('ConsultaD/', views.ConsultaD, name="ConsultaD"),
    path('Notas/', views.Register_Notas, name="Notas"),
    path('ConsultaN/', views.ConsultaN, name="ConsultaN"),
    
    
    #---Estos Permiten Actualizar la informacion
    
    path('Actualizar_Docs/<int:id>/', views.Actualizar_Docs, name="Actualizar_Docs"), 
    
    path('Actualizar_Notas/<int:id>/', views.Actualizar_Notas, name="Actualizar_Notas"), 
    
    
    #---Estos Permiten Eliminar la informacion
    
    path('Eliminar_Docs/<int:id>/', views.Eliminar_Docs, name="Eliminar_Docs"),
    
    path('Eliminar_Notas/<int:id>/', views.Eliminar_Notas, name="Eliminar_Notas"),
]


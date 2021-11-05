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
from django.urls import path
from . import views
from .views import Consulta_PA

urlpatterns = [
    
#---Estas son los LINKS/ENLACES de las Consultas de los Estudiantes
 
    path('Consulta_Es/', views.Consulta_Es, name="Consulta_Es"),
    path('C_nombres/', views.C_nombres, name="C_nombres"),
    path('C_apellidos/', views.C_apellidos, name="C_apellidos"),   
    path('C_grados/', views.C_grados, name="C_grados"),
    path('C_secciones/', views.C_secciones, name="C_secciones"), 
    
#---Estas son los LINKS/ENLACES de las Consultas del Personal Administrativo 
  
    path('Consulta_PA/', views.Consulta_PA, name="Consulta_PA"), 
    path('C_nombres_pa/', views.C_nombres_pa, name="C_nombres_pa"),
    path('C_apellidos_pa/', views.C_apellidos_pa, name="C_apellidos_pa"),   
    path('C_cedula_pa/', views.C_cedula_pa, name="C_cedula_pa"),
    path('C_cargo_pa/', views.C_cargo_pa, name="C_cargo_pa"), 
    
#---Estas son los LINKS/ENLACES de las Consultas del Personal Docente   
 
    path('Consulta_PD/', views.Consulta_PD, name="Consulta_PD"), 
    path('C_nombres_pd/', views.C_nombres_pd, name="C_nombres_pd"),
    path('C_apellidos_pd/', views.C_apellidos_pd, name="C_apellidos_pd"),   
    path('C_cedula_pd/', views.C_cedula_pd, name="C_cedula_pd"),
    path('C_materia_pd/', views.C_materia_pd, name="C_materia_pd"), 
    
    
    
    #---Estos Permiten Actualizar la informacion
    
    path('Actualizar_Es/<int:id>/', views.Actualizar_Es, name="Actualizar_Es"),    
    path('Actualizar_PA/<int:id>/', views.Actualizar_PA, name="Actualizar_PA"),   
    path('Actualizar_PD/<int:id>/', views.Actualizar_PD, name="Actualizar_PD"),


    #---Estos Permiten Eliminar la informacion 
    
    path('Eliminar_Es/<int:id>/', views.Eliminar_Es, name="Eliminar_Es"),   
    path('Eliminar_PA/<int:id>/', views.Eliminar_PA, name="Eliminar_PA"), 
    path('Eliminar_PD/<int:id>/', views.Eliminar_PD, name="Eliminar_PD"), 
    
    
    #---Estos Permiten Ver la informacion de los Estudiantes
    
    path('Ver_Es/<int:id>/', views.Ver_Es, name="Ver_Es"),    
    path('Ver_PA/<int:id>/', views.Ver_PA, name="Ver_PA"),   
    path('Ver_PD/<int:id>/', views.Ver_PD, name="Ver_PD"),

      
      
      
]





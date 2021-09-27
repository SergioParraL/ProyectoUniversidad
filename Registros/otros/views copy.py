from django.shortcuts import render, redirect
from Registros.forms import EstRegistro
from .models import Estudiantes

# Create your views here.

def Registro_Est(request):

    if request.method=="POST":
        form=EstRegistro(data=request.POST)

        if form==Es.is_valid():

            nombres=request.POST.get("nombres")
            apellidoss=request.POST.get("apellidos")
            cedula=request.POST.get("cedula")
            Foto=request.POST.get("Foto")   
            edad=request.POST.get("edad")         
            altura=request.POST.get("altura")
            peso=request.POST.get("peso")
            talla_zapato=request.POST.get("talla_zapato")
            talla_camisa=request.POST.get("talla_camisa")
            talla_pantalon=request.POST.get("talla_pantalon")
            grado=request.POST.get("grado")
            seccion=request.POST.get("seccion")           
            
            query_creation=Estudiantes.objects.create(nombres='nombres', apellidos='apellidos', cedula='cedula', edad='edad', altura='altura', peso='peso', talla_zapato='talla_zapato', talla_camisa='talla_camisa', talla_pantalon='talla_pantalon', grado='grado', seccion='seccion')

            return redirect("/Registro_Est/?valido")

    else:
        
        miform=EstRegistro()

    return render(request, "registros/Registro_Estudiantes.html", {"form":miform})


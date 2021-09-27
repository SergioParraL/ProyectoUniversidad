from django.shortcuts import render, redirect

#BBDD----------------
from .forms import RegistroPA, RegistroPD, RegistroRep, RegistroEst

#FormsModels----------------
from .models import PersonalAdm, PersonalDocente, Representantes, Estudiantes

#Auth----------------
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def Registro_Est(request):
    
    if request.user.is_PA == True:
        if request.user.is_active == True:
            if request.method == 'GET':
                form = RegistroEst()
                contx={
                    'form':form
                }
                
            else:  
                form = RegistroEst(request.POST, request.FILES)
                contx = {
                    'form':form
                }
                if form.is_valid():
                    form.save()
                    return redirect('../../Registro/Registro_Es/?valido')

            messages.success(request, f'Usuario Autorizado: {request.user.username}')
            return render(request, 'registros/Registro_Estudiantes.html', contx)

    messages.error(request, f'El Usuario {request.user.username} No es un Usuario PA ("Personal Administrativo")') 
    return redirect('Home')

@login_required
def Registro_Rep(request):

    if request.user.is_PA == True:
        if request.user.is_active == True:
            if request.method == 'GET':
                form = RegistroRep()  
                contx={
                    'form':form
                }
                
            else:  
                form = RegistroRep(request.POST, request.FILES)
                contx = {
                    'form':form
                }
                
                if form.is_valid():
                    form.save()
                    return redirect('../../Registro/Registro_Es/?valido2')

            return render(request, 'registros/Registro_Rep.html', contx)

    messages.error(request, f'El Usuario {request.user.username} No es un Usuario PA ("Personal Administrativo")') 
    return redirect('Home')


@login_required
def Registro_PA(request):

    if request.user.is_PA == True:
        if request.user.is_active == True:
            if request.method == 'GET':
                form = RegistroPA()
                contx={
                    'form':form
                }
                
            else:
                form = RegistroPA(request.POST, request.FILES)
                contx = {
                    'form':form
                }

                if form.is_valid():
                    form.save()
                    return redirect('../Registro_PA/?valido')
                
            return render(request, 'registros/Registro_PA.html', contx)

    messages.error(request, f'El Usuario {request.user.username} No es un Usuario PA ("Personal Administrativo")') 
    return redirect('Home')

@login_required
def Registro_PD(request):
    
    if request.user.is_PD == True:
        if request.user.is_active == True:
            if request.method == 'GET':
                form = RegistroPD()
                contx={
                    'form':form
                }
                
            else:
                form = RegistroPD(request.POST, request.FILES)
                contx = {
                    'form':form
                }
                
                
                if form.is_valid():
                    form.save()
                    return redirect('../../Registro/Registro_PD/?valido')

            return render(request, 'registros/Registro_PD.html', contx)

    messages.error(request, f'El Usuario {request.user.username} No es un Usuario PD ("Personal Docente")') 
    return redirect('Home')
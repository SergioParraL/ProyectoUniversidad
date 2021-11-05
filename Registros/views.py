from django.shortcuts import render, redirect

#BBDD----------------
from .forms import RegistroPA, RegistroPD, RegistroRep, RegistroEst, registerProfilePA, registerProfilePD
from Institucion.forms import UserRegisterForm_PA,UserRegisterForm_PD
from Institucion.models import SystemUser, PA_profile, PD_profile

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
            id = request.user.id
            paUser = SystemUser.objects.get(id = id)
            paProfile=PA_profile.objects.get(usuario_id=id)
            if request.method == 'GET':
                form = registerProfilePA(instance=paProfile)
                form2 = UserRegisterForm_PA(instance= paUser)
                contx={
                    'form':form, 'form2':form2
                }
                
            else:
                form = registerProfilePA(request.POST, request.FILES, instance=paProfile)
                form2 = UserRegisterForm_PA(request.POST, request.FILES, instance= paUser)
                contx = {
                    'form':form, 'form2':form2
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
            pa = PersonalAdm.objects.get(id = request.user.id)
            if request.method == 'GET':
                form = registerProfilePD()
                form2 = UserRegisterForm_PD(instance= pa)
                contx={
                    'form':form, 'form2':form2
                }
                
            else:
                form = registerProfilePD(request.POST, request.FILES)
                form2 = UserRegisterForm_PD(request.POST, request.FILES, instance = pa)
                contx = {
                    'form':form, 'form2':form2
                }
                
                
                if form.is_valid():
                    form.save()
                    return redirect('../../Registro/Registro_PD/?valido')

            return render(request, 'registros/Registro_PD.html', contx)

    messages.error(request, f'El Usuario {request.user.username} No es un Usuario PD ("Personal Docente")') 
    return redirect('Home')




                #ver = pdProfile.__dict__['_query'].__dict__
            #ver2 = pdUser.__dict__
            #ver3 = pdProfile.__dict__['_query'].__dict__['model'].__dict__
            #ver4 = pdProfile.__dict__['_query'].__dict__['model'].__dict__['usuario'].__dict__['field'].__dict__
            
            #where es el filttro

            #ver3 = pdProfile.__dict__['_query'].__dict__['where'].__dict__
            #ver4 = pdProfile.__dict__['_query'].__dict__['where'].__dict__['children'][0].__dict__


            #---- Prueba

            #ver3 = pdProfile.__dict__['_query'].__dict__['_constructor_args'][0][0].__dict__
            #ver4 = pdProfile.__dict__['_query'].__dict__['_constructor_args'][0][0].__dict__['usuario_id'].__dict__['field'].__dict__['opts'].__dict__['_get_fields_cache']

            #

            #ver2 = pdProfile.query.__dict__

            #ver3 = pdProfile.__dict__['_iterable_class'].__dict__

            #ver4 = pdProfile.__dict__['_iterable_class'].__dict__['__iter__'].__dict__

            #ver5 = pdProfile.__dict__['_query'].__dict__['alias_map']['Institucion_pd_profile'].__dict__
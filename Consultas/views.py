from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.core import serializers
import json

#BBDD----------------
from Registros.models import Estudiantes, PersonalAdm, PersonalDocente, Representantes
from Institucion.models import SystemUser, PA_profile, PD_profile

#FormsModels----------------
from Registros.forms import RegistroPA, RegistroPD, RegistroRep, RegistroEst, registerProfilePA, registerProfilePD
from Institucion.forms import UserRegisterForm_PA,UserRegisterForm_PD

#Auth----------------
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


#---Estas son las vistas de las Consultas a la BBDD de los Estudiantes  

#---- Funciones Globales -------
#
""" def Filter( estid = []):
    for m in filterGradoSeccion():
        Grados_list = [
            
            ('1ero'),
            ('2do'),
            ('3ro'),
            ('4to'),
            ('5to'),
            ('6to'),
        ]
        Ver = m
        Grado = m[1] - 1
        select_grado = Grados_list[Grado]

        Secciones_list = [
            
            ('A'),
            ('B'),
            ('C'),
            ('D'),
            ('E'),
            ('F'),
            ('G'),
            ('H'),
        ]

        Seccion = m[2] - 1
        select_sec = Secciones_list[Seccion]
        estid.append([m[0],select_grado,select_sec ])
        #Filters = [select_grado,select_sec]
    return estid

def filterGradoSeccion( estid = []):

    for n in Estudiantes.objects.all():
        #filter = filterGradoSeccion(n)
        estid.append([n.id,n.grado,n.seccion ])

    return estid """
def filterGradoSeccion(estudiantes):
        estid = []
        if estudiantes:
            for n in estudiantes:
                Grados_list = [
                    
                    ('1ero'),
                    ('2do'),
                    ('3ro'),
                    ('4to'),
                    ('5to'),
                    ('6to'),
                ]

                Grado = n.grado - 1
                select_grado = Grados_list[Grado]


                Secciones_list = [
                    
                    ('A'),
                    ('B'),
                    ('C'),
                    ('D'),
                    ('E'),
                    ('F'),
                    ('G'),
                    ('H'),
                ]

                Seccion = n.seccion - 1
                select_sec = Secciones_list[Seccion]
                estid.append([n.id,select_grado,select_sec ])
                estid_ordenado = sorted(estid)


            select_grado = estid_ordenado
            select_sec = estid_ordenado
            return estid_ordenado
        else:
            result = None
        return result


def filterMateriasEsp(PD_ME):
        pdid = []
        if PD_ME:
            for n in PD_ME:
                Materias_list = [
                    
                    ('Lenguaje'),
                    ('Comunicación y Cultura'),
                    ('Ciencias Naturales y Sociedad'),
                    ('Ciencias Sociales'),
                    ('Ciudadanía e Identidad'),
                    ('Educación Física, deporte y Recreación'),
                    ('Matemática'),
                ] 

                Materia = n.materia - 1
                select_materia = Materias_list[Materia]


                Especialidades_list = [
                    
                    ('Desarrollo Endogeno'),
                    ('Educación Física'),
                    ('Música'),
                    ('Teatro'),
                    ('Danza'),
                    ('Manualidades'),
                    ('Aula Integrada'),
                    ('Producción'),
                    ('CRA (Centro de Recursos para el Aprendizaje)'),
                ] 

                Esp = n.especialidades - 1
                select_esp = Especialidades_list[Esp]
                pdid.append([n.id,select_materia,select_esp ])
                pdid_ordenado = sorted(pdid)

            return pdid_ordenado
        else:
            result = None
        return result



@login_required
def Consulta_Es(request):
    
    if request.method == 'POST':
        nombres = request.POST.get("buscar_nombres")
        apellidos = request.POST.get("buscar_apellidos")
        grado = request.POST.get("buscar_grado")
        seccion = request.POST.get("buscar_seccion")
        estudiantes=Estudiantes.objects.filter(nombres__icontains=nombres, apellidos__icontains=apellidos, grado__icontains=grado, seccion__icontains=seccion)
        filterValues = filterGradoSeccion(Estudiantes.objects.filter(nombres__icontains=nombres, apellidos__icontains=apellidos, grado__icontains=grado, seccion__icontains=seccion))
        if filterValues:
            filterValues = filterValues
        else:
            filterValues = 'noMatch'
        ctx= { 

            'estudiantes':estudiantes, 'Filtro':filterValues, 
        }
        return render(request, "consultas/ESTUDIANTES/Consulta_Estudiantes.html", ctx)
    
    else:       
        estudiantes=Estudiantes.objects.all()
        filterValues = filterGradoSeccion(Estudiantes.objects.all())
        if filterValues:
            filterValues = filterValues
        else:
            filterValues = 'noMatch'
        ctx= { 

            'estudiantes':estudiantes, 'Filtro':filterValues, 
        }
        return render(request, "consultas/ESTUDIANTES/Consulta_Estudiantes.html", ctx)

@login_required
def C_nombres(request):
    
    if request.method == 'POST':
        nombres = request.POST.get("buscar_nombres") 
        estudiantes=Estudiantes.objects.filter(nombres__icontains=nombres)
        filterValues = filterGradoSeccion(Estudiantes.objects.filter(nombres__icontains=nombres))
        if filterValues:
            filterValues = filterValues
        else:
            filterValues = 'noMatch'
        ctx= { 

            'estudiantes':estudiantes, 'Filtro':filterValues, 
        }
        return render(request, "consultas/ESTUDIANTES/C_nombres.html", ctx)
    
    else:        
        estudiantes=Estudiantes.objects.all()
        filterValues = filterGradoSeccion(Estudiantes.objects.all())
        if filterValues:
            filterValues = filterValues
        else:
            filterValues = 'noMatch'
        ctx= { 

            'estudiantes':estudiantes, 'Filtro':filterValues, 
        }

        filterValues=filterValues.clear
        return render(request, "consultas/ESTUDIANTES/C_nombres.html", ctx)


@login_required
def C_apellidos(request):
    
    if request.method == 'POST':   
        apellidos = request.POST.get("buscar_apellidos")
        estudiantes=Estudiantes.objects.filter(apellidos__icontains=apellidos)
        filterValues = filterGradoSeccion(Estudiantes.objects.filter(apellidos__icontains=apellidos))
        if filterValues:
            filterValues = filterValues
        else:
            filterValues = 'noMatch'
        ctx= { 

            'estudiantes':estudiantes, 'Filtro':filterValues, 
        }
        return render(request, "consultas/ESTUDIANTES/C_apellidos.html",ctx)

    else:         
        estudiantes=Estudiantes.objects.all()
        filterValues = filterGradoSeccion(Estudiantes.objects.all())
        if filterValues:
            filterValues = filterValues
        else:
            filterValues = 'noMatch'
        ctx= { 

            'estudiantes':estudiantes, 'Filtro':filterValues, 
        }
        return render(request, "consultas/ESTUDIANTES/C_apellidos.html", ctx)
    
@login_required   
def C_grados(request):
    
    if request.method == 'POST':
        grado = request.POST.get("buscar_grado")
        estudiantes=Estudiantes.objects.filter(grado__icontains=grado)
        filterValues = filterGradoSeccion(Estudiantes.objects.filter(grado__icontains=grado))
        if filterValues:
            filterValues = filterValues
        else:
            filterValues = 'noMatch'
        ctx= { 

            'estudiantes':estudiantes, 'Filtro':filterValues, 
        }
        return render(request, "consultas/ESTUDIANTES/C_grados.html", ctx)
    
    else:       
        estudiantes=Estudiantes.objects.all()
        filterValues = filterGradoSeccion(Estudiantes.objects.all())
        if filterValues:
            filterValues = filterValues
        else:
            filterValues = 'noMatch'
        ctx= { 

            'estudiantes':estudiantes, 'Filtro':filterValues, 
        }
        return render(request, "consultas/ESTUDIANTES/C_grados.html", ctx)
    
    
@login_required  
def C_secciones(request):
    
    if request.method == 'POST':
        seccion = request.POST.get("buscar_seccion")
        estudiantes=Estudiantes.objects.filter(seccion__icontains=seccion)
        filterValues = filterGradoSeccion(Estudiantes.objects.filter(seccion__icontains=seccion))
        if filterValues:
            filterValues = filterValues
        else:
            filterValues = 'noMatch'
        ctx= { 

            'estudiantes':estudiantes, 'Filtro':filterValues, 
        }
        return render(request, "consultas/ESTUDIANTES/C_secciones.html", ctx)
    
    else:        
        estudiantes=Estudiantes.objects.all()
        filterValues = filterGradoSeccion(Estudiantes.objects.all())
        if filterValues:
            filterValues = filterValues
        else:
            filterValues = 'noMatch'
        ctx= { 

            'estudiantes':estudiantes, 'Filtro':filterValues, 
        }
        return render(request, "consultas/ESTUDIANTES/C_secciones.html", ctx)
    
#---Estas son las vistas de las Consultas a la BBDD del Personal Administrativo     
     
@login_required 
def Consulta_PA(request):

    if request.user.is_PA == True:
        if request.user.is_active == True:
            if request.method == 'POST':
                nombres = request.POST.get("buscar_nombres")
                apellidos = request.POST.get("buscar_apellidos")
                cedula = request.POST.get("buscar_cedula")
                cargo = request.POST.get("buscar_cargo")
                PA=PA_profile.objects.filter(nombres__icontains=nombres, apellidos__icontains=apellidos, cedula__icontains=cedula, cargo__icontains=cargo)
                return render(request, "consultas/PA/Consulta_PA.html", {'PA':PA})
            
            else:        
                PA=PA_profile.objects.all()
                ctx= { 
                    
                    "PA": PA
                }
                return render(request, "consultas/PA/Consulta_PA.html", ctx)

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Consultar') 
    return redirect('Home')

@login_required
def C_nombres_pa(request):
        
    if request.user.is_PA == True:
        if request.user.is_active == True:
            if request.method == 'POST':
                nombres = request.POST.get("buscar_nombres")
                PA=PA_profile.objects.filter(nombres__icontains=nombres)
                return render(request, "consultas/PA/C_nombres_pa.html", {"PA": PA})
            
            else:        
                PA=PA_profile.objects.all()
                ctx= { 
                    'PA':PA
                }
                return render(request, "consultas/PA/C_nombres_pa.html", ctx)

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Consultar')
    return redirect('Home')
    
@login_required
def C_apellidos_pa(request):
    
    if request.user.is_PA == True:
        if request.user.is_active == True:
            if request.method == 'POST':
                apellidos = request.POST.get("buscar_apellidos")
                PA=PA_profile.objects.filter(apellidos__icontains=apellidos)
                return render(request, "consultas/PA/C_apellidos_pa.html", {"PA": PA})
            
            else:         
                PA=PA_profile.objects.all()
                ctx= {
                    
                    'PA':PA
                }
                return render(request, "consultas/PA/C_apellidos_pa.html", ctx)

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Consultar')
    return redirect('Home')

@login_required
def C_cedula_pa(request):
    
    if request.user.is_PA == True:
        if request.user.is_active == True:
            if request.method == 'POST':
                cedula = request.POST.get("buscar_cedula")
                PA=PA_profile.objects.filter(cedula__icontains=cedula)
                return render(request, "consultas/PA/C_cedula_pa.html", {"PA": PA})
            
            else:        
                PA=PA_profile.objects.all()
                ctx= {   
                    'PA':PA
                }
                return render(request, "consultas/PA/C_cedula_pa.html", ctx)
    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Consultar')
    return redirect('Home')

@login_required
def C_cargo_pa(request):
    
    if request.user.is_PA == True:
        if request.user.is_active == True:
            if request.method == 'POST':
                cargo = request.POST.get("buscar_cargo")
                PA=PA_profile.objects.filter(cargo__icontains=cargo)
                return render(request, "consultas/PA/C_cargo_pa.html", {"PA": PA})
            
            else:       
                PA=PA_profile.objects.all()
                ctx= { 
                    'PA':PA
                }
                return render(request, "consultas/PA/C_cargo_pa.html", ctx)

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Consultar')
    return redirect('Home')

#---Estas son las vistas de las Consultas a la BBDD del Personal Docente    

@login_required 
def Consulta_PD(request):

    if request.user.is_PA == True:
        if request.user.is_active == True:
            if request.method == 'POST':       
                nombres = request.POST.get("buscar_nombres")
                apellidos = request.POST.get("buscar_apellidos")
                cedula = request.POST.get("buscar_cedula")
                materia = request.POST.get("buscar_materia")   
                especialidades = request.POST.get("buscar_especialidades")      
                PD=PD_profile.objects.filter(nombres__icontains=nombres, apellidos__icontains=apellidos, cedula__icontains=cedula, materia__icontains=materia, especialidades__icontains=especialidades)               
                
                #-----Filter de Campos Especiales ----------
                filterValues = filterMateriasEsp(PD)
                if filterValues:
                    filterValues = filterValues
                else:
                    filterValues = 'noMatch'
                ctx= { 

                    "PD": PD, 'Filtro':filterValues, 
                }
                
                return render(request, "consultas/PD/Consulta_PD.html", ctx)

            else:              
                PD=PD_profile.objects.all() 

                #-----Filter de Campos Especiales ----------       
                filterValues = filterMateriasEsp(PD)
                if filterValues:
                    filterValues = filterValues
                else:
                    filterValues = 'noMatch'
                ctx= { 
                    
                    "PD": PD, 'Filtro':filterValues, 
                }
                return render(request, "consultas/PD/Consulta_PD.html", ctx)

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Consultar') 
    return redirect('Home')
    
@login_required
def C_nombres_pd(request):

    if request.user.is_PA == True:
        if request.user.is_active == True:
            if request.method == 'POST':                
                nombres = request.POST.get("buscar_nombres")       
                PD=PD_profile.objects.filter(nombres__icontains=nombres)               
                
                #-----Filter de Campos Especiales ----------       
                filterValues = filterMateriasEsp(PD)
                if filterValues:
                    filterValues = filterValues
                else:
                    filterValues = 'noMatch'
                ctx= { 
                    
                    "PD": PD, 'Filtro':filterValues, 
                }
                return render(request, "consultas/PD/C_nombres_pd.html", ctx)
                           
            else:                       
                PD=PD_profile.objects.all()               
                #-----Filter de Campos Especiales ----------       
                filterValues = filterMateriasEsp(PD)
                if filterValues:
                    filterValues = filterValues
                else:
                    filterValues = 'noMatch'
                ctx= { 
                    
                    "PD": PD, 'Filtro':filterValues, 
                }             
                return render(request, "consultas/PD/C_nombres_pd.html", ctx)

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Consultar') 
    return redirect('Home')

@login_required
def C_apellidos_pd(request):
    
    if request.user.is_PA == True:
        if request.user.is_active == True:
            if request.method == 'POST':                            
                apellidos = request.POST.get("buscar_apellidos")
                PD=PD_profile.objects.filter(apellidos__icontains=apellidos)                
                
                #-----Filter de Campos Especiales ----------       
                filterValues = filterMateriasEsp(PD)
                if filterValues:
                    filterValues = filterValues
                else:
                    filterValues = 'noMatch'
                ctx= { 
                    
                    "PD": PD, 'Filtro':filterValues, 
                }
                return render(request, "consultas/PD/C_apellidos_pd.html", ctx)

            else:                        
                PD=PD_profile.objects.all()                
                #-----Filter de Campos Especiales ----------       
                filterValues = filterMateriasEsp(PD)
                if filterValues:
                    filterValues = filterValues
                else:
                    filterValues = 'noMatch'
                ctx= { 
                    
                    "PD": PD, 'Filtro':filterValues, 
                }          
                return render(request, "consultas/PD/C_apellidos_pd.html", ctx)

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Consultar') 
    return redirect('Home')

@login_required
def C_cedula_pd(request):

    if request.user.is_PA == True:
        if request.user.is_active == True:
            if request.method == 'POST':            
                cedula = request.POST.get("buscar_cedula")                        
                PD=PD_profile.objects.filter(cedula__icontains=cedula)                
                
                #-----Filter de Campos Especiales ----------       
                filterValues = filterMateriasEsp(PD)
                if filterValues:
                    filterValues = filterValues
                else:
                    filterValues = 'noMatch'
                ctx= { 
                    
                    "PD": PD, 'Filtro':filterValues, 
                }
                return render(request, "consultas/PD/C_cedula_pd.html", ctx)

            else:                        
                PD=PD_profile.objects.all()                
                #-----Filter de Campos Especiales ----------       
                filterValues = filterMateriasEsp(PD)
                if filterValues:
                    filterValues = filterValues
                else:
                    filterValues = 'noMatch'
                ctx= { 
                    
                    "PD": PD, 'Filtro':filterValues, 
                }              
                return render(request, "consultas/PD/C_cedula_pd.html", ctx)

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Consultar') 
    return redirect('Home')


@login_required
def C_materia_pd(request):

    if request.user.is_PA == True:
        if request.user.is_active == True:    
            if request.method == 'POST':                            
                materia = request.POST.get("buscar_materia")        
                PD=PD_profile.objects.filter(materia__icontains=materia)                
                
                #-----Filter de Campos Especiales ----------       
                filterValues = filterMateriasEsp(PD)
                if filterValues:
                    filterValues = filterValues
                else:
                    filterValues = 'noMatch'
                ctx= { 
                    
                    "PD": PD, 'Filtro':filterValues, 
                }
                return render(request, "consultas/PD/C_materia_pd.html", ctx)

            else:                        
                PD=PD_profile.objects.all()                
                #-----Filter de Campos Especiales ----------       
                filterValues = filterMateriasEsp(PD)
                if filterValues:
                    filterValues = filterValues
                else:
                    filterValues = 'noMatch'
                ctx= { 
                    
                    "PD": PD, 'Filtro':filterValues, 
                }             
                return render(request, "consultas/PD/C_materia_pd.html", ctx)

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Consultar') 
    return redirect('Home')  



@login_required
def C_especialidades_pd(request):

    if request.user.is_PA == True:
        if request.user.is_active == True:    
            if request.method == 'POST':       
                especialidades = request.POST.get("buscar_especialidades")        
                PD=PD_profile.objects.filter(especialidades__icontains=especialidades)                            
                
                #-----Filter de Campos Especiales ----------       
                filterValues = filterMateriasEsp(PD)
                if filterValues:
                    filterValues = filterValues
                else:
                    filterValues = 'noMatch'
                ctx= { 
                    
                    "PD": PD, 'Filtro':filterValues, 
                }
                return render(request, "consultas/PD/C_especialidades_pd.html", ctx)

            else:                        
                PD=PD_profile.objects.all()                
                #-----Filter de Campos Especiales ----------       
                filterValues = filterMateriasEsp(PD)
                if filterValues:
                    filterValues = filterValues
                else:
                    filterValues = 'noMatch'
                ctx= { 
                    
                    "PD": PD, 'Filtro':filterValues, 
                }             
                return render(request, "consultas/PD/C_especialidades_pd.html", ctx)

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Consultar') 
    return redirect('Home')



#---Esta Vista Permite la Edicion del Registro de los Estudiantes   

@login_required 
def Actualizar_Es(request, id):

    if request.user.is_PA == True:
        if request.user.is_active == True: 
            estudiante = Estudiantes.objects.get(id = id)            
            if request.method == 'GET':            
                form = RegistroEst(instance= estudiante)
                contx={
                    'form':form, 'estudiante':estudiante
                }

            else:                
                form = RegistroEst(request.POST, request.FILES, instance=estudiante)
                if form.is_valid():
                    form.save()
                    return redirect("Consulta_Es")

            return render(request, "consultas/ESTUDIANTES/Actualizar_Estudiantes.html", contx)

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Actualizar Datos de los Estudiantes') 
    return redirect('Home')  
        
#---Esta Vista Permite la Edicion del Registro del Personal Administrativo  

@login_required
def Actualizar_PA(request, id):

    if request.user.is_PA == True:
        if request.user.is_active == True:    
            paUser = SystemUser.objects.get(id = id)
            if request.method == 'GET':
                if PA_profile.objects.filter(usuario_id=id):

                    paProfile=PA_profile.objects.get(usuario_id=id)
                    form = registerProfilePA(instance= paProfile)

                else:
                    form = registerProfilePA()
                    paProfile=None

                form2 =UserRegisterForm_PA(instance= paUser)               
                contx={
                    'form':form, 'form2':form2, 'pa':paProfile
                }

            else:
                if PA_profile.objects.filter(usuario_id=id):
                    paProfile=PA_profile.objects.get(usuario_id=id)
                    form = registerProfilePA(request.POST, request.FILES,instance=paProfile)
                else:
                    form = registerProfilePA(request.POST, request.FILES)
                    
                form2 = UserRegisterForm_PA(request.POST, request.FILES, instance=paUser)
                if form.is_valid():
                    form.save()
                    return redirect(f"../{request.user.id}/?valido")

            return render(request, "consultas/PA/Actualizar_PA.html", contx)

    messages.error(request, f'El Usuario {request.user.username} No es un Usuario PA ("Personal Administrativo")') 
    return redirect('Home')  


#---Esta Vista Permite la Edicion del Registro del Personal Docente  

@login_required
def Actualizar_PD(request, id):

    if request.user.is_PD == True:
        if request.user.is_active == True:   
            pdUser = SystemUser.objects.get(id = id)
            if request.method == 'GET':
                if PD_profile.objects.filter(usuario_id=id):

                    pdProfile=PD_profile.objects.get(usuario_id=id)
                    form = registerProfilePD(instance= pdProfile)

                else:
                    form = registerProfilePD()
                    pdProfile=None

                form2 =UserRegisterForm_PD(instance= pdUser)               
                contx={
                    'form':form, 'form2':form2, 'pd':pdProfile
                }

            else:
                if PD_profile.objects.filter(usuario_id=id):
                    pdProfile=PD_profile.objects.get(usuario_id=id)
                    form = registerProfilePD(request.POST, request.FILES,instance=pdProfile)
                else:
                    form = registerProfilePD(request.POST, request.FILES)
                    
                form2 = UserRegisterForm_PD(request.POST, request.FILES, instance=pdUser)
                if form.is_valid():
                    form.save()
                    return redirect(f"../{request.user.id}/?valido")

            return render(request, "consultas/PD/Actualizar_PD.html", contx)

    messages.error(request, f'El Usuario {request.user.username} No es un Usuario PD ("Personal Docente")')
    return redirect('Home')

#---Esta Vista Permite la ELIMINAR el Registro de los Estudiantes

@login_required
def Eliminar_Es(request, id):
    
    if request.user.is_PA == True:
        if request.user.is_active == True:
            estudiante = Estudiantes.objects.get(id = id)
            estudiante.delete()
            return redirect("Consulta_Es")

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Eliminar Datos de los Estudiantes')
    return redirect('Home')

#---Esta Vista Permite la ELIMINAR el Registro del Personal Administrtivo // En observacion para eliminar

@login_required
def Eliminar_PA(request, id):
    
    if request.user.is_PA == True:
        if request.user.is_active == True:
            pa = PersonalAdm.objects.get(id = id)
            pa.delete()
            return redirect("Consulta_PA")

    messages.error(request, f'El Usuario {request.user.username} No es un Usuario PA ("Personal Administrativo")')
    return redirect('Home')

#---Esta Vista Permite la ELIMINAR el Registro del Personal Docente // En observacion para eliminar

@login_required
def Eliminar_PD(request, id):
    
    if request.user.is_PD == True:
        if request.user.is_active == True:
            pd = PersonalDocente.objects.get(id = id)
            pd.delete()
            return redirect("Consulta_PD")

    messages.error(request, f'El Usuario {request.user.username} No es un Usuario PD ("Personal Docente")')
    return redirect('Home')


#---Esta Vista Permite la VER el Registro de los Estudiantes   

@login_required
def Ver_Es(request, id):
    
    if request.method == 'GET':
        Ver = Estudiantes.objects.get(id = id)
        Grados_list = [
            
            ('1ero'),
            ('2do'),
            ('3ro'),
            ('4to'),
            ('5to'),
            ('6to'),
        ]

        Grado = Ver.grado - 1
        select_grado = Grados_list[Grado]


        Secciones_list = [
            
            ('A'),
            ('B'),
            ('C'),
            ('D'),
            ('E'),
            ('F'),
            ('G'),
            ('H'),
        ]

        Seccion = Ver.seccion - 1
        select_sec = Secciones_list[Seccion]

        contx={
            'Ver':Ver, 'Grado':select_grado, 'Seccion':select_sec
        }

    return render(request, "consultas/ESTUDIANTES/Ver_Estudiantes.html", contx)

#---Esta Vista Permite la VER el Registro del Personal Administrtivo // OJO MODIFICACION PARA QUE SEA UN USER

@login_required
def Ver_PA(request, id):
    
    if request.user.is_PA == True:
        if request.user.is_active == True:
            if request.method == 'GET':
                Ver = PA_profile.objects.get(id = id)
                contx={
                    'Ver':Ver
                }
            return render(request, "consultas/PA/Ver_PA.html", contx)

    messages.error(request, f'El Usuario {request.user.username} No es un Usuario PA ("Personal Administrativo")')
    return redirect('Home')

#---Esta Vista Permite la VER el Registro del Personal Administrtivo  // OJO MODIFICACION PARA QUE SEA UN USER

@login_required
def Ver_PD(request, id):
    
    if request.method == 'GET':
        Ver = PD_profile.objects.get(id = id)
        contx={
            'Ver':Ver
        }

    return render(request, "consultas/PD/Ver_PD.html", contx)
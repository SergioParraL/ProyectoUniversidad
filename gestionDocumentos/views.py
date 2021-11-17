from django.shortcuts import render, redirect

#BBDD----------------
from .models import DocsDB, NotasDB

#FormsModels----------------
from .forms import Docs, Notas
from Institucion.models import SystemUser, PA_profile, PD_profile

#Auth----------------
from django.contrib.auth.decorators import login_required

#Messages----------------
from django.contrib import messages

#---- Funciones Globales -------
#

def filterGradoSeccion(notas):
        notasid = []
        if notas:
            for n in notas:
                Grados_list = [
                    
                    ('1ero'),
                    ('2do'),
                    ('3ro'),
                    ('4to'),
                    ('5to'),
                    ('6to'),
                ]

                Grado = n.Grado - 1
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

                Seccion = n.Seccion - 1
                select_sec = Secciones_list[Seccion]

                Momentos_list = [
                    
                    ('I'),
                    ('II'),
                    ('III'),
                ]  

                Momento = n.Momento - 1
                select_Momento = Momentos_list[Momento]
                notasid.append([n.id,select_grado,select_sec,select_Momento ])
                notasid_ordenado = sorted(notasid)
                
            return notasid_ordenado
        else:
            result = None
        return result


def filterTipoFormat_Docs(docs):
        docsid = []
        if docs:
            for n in docs:
                Docs_tipo = [
                    
                    ('Boletin'),
                    ('Constancia'),
                    ('Planilla'),
                    ('Convocatoria'),
                    ('Otro'),
                ]
                Tipo = n.Tipo - 1
                select_Tipo = Docs_tipo[Tipo]


                Docs_format = [
                    
                    ('Word'),
                    ('Excel'),
                    ('PowerPoint'),
                    ('PDF'),
                    ('LibreOffice'),
                    ('Otro'),
                ]

                Format = n.Formato - 1
                select_Format = Docs_format[Format]
                docsid.append([n.id,select_Tipo,select_Format ])
                docsid_ordenado = sorted(docsid)

            return docsid_ordenado
        else:
            result = None
        return result




#---Esta Vista Permite Registrar los Documentos

@login_required
def Register_Docs(request):

    if request.user.is_PA == True:
        if request.user.is_active == True:
            if request.method == 'GET':
                form = Docs()
                contx={
                    'form':form
                }

            else:
                form = Docs(request.POST, request.FILES)
                contx = {
                    'form':form
                }    
                if form.is_valid():
                    form.save()
                    return redirect('../../Gestion/Docs/?valido')

            messages.success(request, f'Usuario Autorizado: {request.user.username}')
            return render(request, 'gestiones/Register_Docs.html', contx)

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Subir Documentos')
    return redirect('Home')

#---Esta Vista Permite Consultar los Documentos

@login_required
def ConsultaD(request):

    if request.user.is_PA == True:
        if request.user.is_active == True:
            if request.method == 'POST':
                documento = request.POST.get("buscar_nombre")
                documento=DocsDB.objects.filter(Nombre_Documento__icontains=documento)
                
                #-----Filter de Campos Especiales ----------
                
                filterValues = filterTipoFormat_Docs(documento)
                if filterValues:
                    filterValues = filterValues
                else:
                    filterValues = 'noMatch'
                ctx= { 

                    'documento':documento, 'Filtro':filterValues, 
                }
                
                return render(request, "gestiones/ConsultaD.html", ctx)

            else:             
                documento = DocsDB.objects.all()
                
                #-----Filter de Campos Especiales ----------
                
                filterValues = filterTipoFormat_Docs(documento)
                if filterValues:
                    filterValues = filterValues
                else:
                    filterValues = 'noMatch'
                ctx= { 

                    'documento':documento, 'Filtro':filterValues, 
                }
            return render(request, "gestiones/ConsultaD.html", ctx)

    messages.error(request, f'El Usuario {request.user.username} No es un Usuario PA ("Personal Administrativo")') 
    return redirect('Home')  

#---Esta Vista Permite Registrar las Notas

@login_required
def Register_Notas(request):
    pdUser= request.user
    if request.user.is_PD == True:
        if request.user.is_active == True:
            if request.method == 'GET':
                queryProfile= PD_profile.objects.filter(usuario_id=pdUser.id)
                if queryProfile:
                    pdProfile = PD_profile.objects.get(usuario_id=pdUser.id)
                    #fasf=sdfasdf
                    form = Notas()
                    contx={
                        'form':form, 'pdProfile':pdProfile
                    }
                else:
                    result = 'noMatch'

                    contx={
                        'result': result
                    }

            else:
                
                form = Notas(request.POST, request.FILES)
                contx = {
                    'form':form
                }
                
                if form.is_valid():
                    form.save()
                    return redirect('../../Gestion/Notas/?valido')

            messages.success(request, f'Usuario Autorizado: {request.user.username}')
            return render(request, 'gestiones/Register_Notas.html', contx)

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Subir Notas')
    return redirect('Home')

#---Esta Vista Permite Consultar las Notas

@login_required
def ConsultaN(request):

    if request.method == 'POST':
        nombre_notas = request.POST.get("buscar_nombre_notas")
        grado = request.POST.get("buscar_grado")
        seccion = request.POST.get("buscar_seccion")
        momento = request.POST.get("buscar_momento")
        notas=NotasDB.objects.filter(Grado__icontains=grado, Seccion__icontains=seccion, Momento__icontains=momento, Nombre_Notas__icontains=nombre_notas)
        
        #-----Filter de Campos Especiales ----------
        
        filterValues = filterGradoSeccion(notas)
        if filterValues:
            filterValues = filterValues
        else:
            filterValues = 'noMatch'
        ctx= { 

            'notas':notas, 'Filtro':filterValues, 
        }
        
        return render(request, "gestiones/ConsultaN.html", ctx)

    else:  
        notas = NotasDB.objects.order_by('id')


        #-----Filter de Campos Especiales ----------
        
        filterValues = filterGradoSeccion(notas)
        #fgd=gds
        if filterValues:
            filterValues = filterValues
        else:
            filterValues = 'noMatch'
        ctx= { 

            'notas':notas, 'Filtro':filterValues, 
        }

    return render(request, "gestiones/ConsultaN.html", ctx)

#---Esta Vista Permite la Edicion del Registro de los Documentos

@login_required   
def Actualizar_Docs(request, id):

    if request.user.is_PA == True:
        if request.user.is_active == True:
            doc = DocsDB.objects.get(id = id)
            if request.method == 'GET':
                form = Docs(instance= doc)
                contx={
                    'form':form,'form2':doc
                }

            else:   
                form = Docs(request.POST, request.FILES, instance=doc)
                if form.is_valid():
                    form.save()
                    messages.success(request, f'Documento {doc.Nombre_Documento} Actualizado Correctamente')
                    return redirect("ConsultaD")

            return render(request, "gestiones/Actualizar_Docs.html", contx)

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Actualizar Documentos')
    return redirect('Home')

#---Esta Vista Permite la Edicion del Registro de la Notas

@login_required    
def Actualizar_Notas(request, id):

    if request.user.is_PD == True:
        if request.user.is_active == True:
            nota= NotasDB.objects.get(id = id)
            queryProfile= PD_profile.objects.filter(usuario_id=request.user.id)
            if queryProfile:
                pdProfile = PD_profile.objects.get(usuario_id=request.user.id)
                if pdProfile.id == nota.PD_Notes_id: 
                    #sad=sdfsd    
                    if request.method == 'GET':
                        form = Notas(instance= nota)
                        contx={
                            'form':form,'pdProfile':pdProfile, 'form2':nota
                        }

                        #sf=sd
                    else:
                        
                        form = Notas(request.POST, request.FILES, instance=nota)
                        if form.is_valid():
                            form.save()
                            messages.success(request, f'Planilla de Notas del Grado {nota.Grado} de la Sección {nota.Seccion} fue Actualizado Correctamente')
                            return redirect("ConsultaN")
                else:
                    result = 'noMatch'

                    contx={
                        'result': result
                    }
            else:
                result = 'noMatchPD'

                contx={
                    'result': result
                }


            return render(request, "gestiones/Actualizar_Notas.html", contx)

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Actualizar Notas')
    return redirect('Home')

@login_required
def Eliminar_Docs(request, id):

    if request.user.is_PA == True:
        if request.user.is_active == True:
            doc = DocsDB.objects.get(id = id)
            doc.delete()
            messages.success(request, f'Documento {doc.Nombre_Documento} Eliminado Correctamente')
            return redirect("ConsultaD")

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Eliminar Documentos')
    return redirect('Home')


@login_required
def Eliminar_Notas(request, id):

    if request.user.is_PD == True:
        if request.user.is_active == True:
            nota = NotasDB.objects.get(id = id)
            nota.delete()
            messages.success(request, f'Planilla de Notas Nro: {nota} Eliminada Correctamente') 
            return redirect("ConsultaN")

    messages.error(request, f'El Usuario {request.user.username} No tiene Permiso para Eliminar Notas')
    return redirect('Home')
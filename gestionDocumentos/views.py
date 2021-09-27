from django.shortcuts import render, redirect

#BBDD----------------
from .models import DocsDB, NotasDB

#FormsModels----------------
from .forms import Docs, Notas

#Auth----------------
from django.contrib.auth.decorators import login_required

#Messages----------------
from django.contrib import messages

# Create your views here.

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
                return render(request, "gestiones/ConsultaD.html", {"documento": documento})

            else:             
                documento = DocsDB.objects.all()
                ctx = {
                    'documento':documento
                }

            return render(request, "gestiones/ConsultaD.html", ctx)

    messages.error(request, f'El Usuario {request.user.username} No es un Usuario PA ("Personal Administrativo")') 
    return redirect('Home')  

#---Esta Vista Permite Registrar las Notas

@login_required
def Register_Notas(request):

    if request.user.is_PD == True:
        if request.user.is_active == True:
            if request.method == 'GET':
                form = Notas()
                contx={
                    'form':form
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
        grado = request.POST.get("buscar_grado")
        seccion = request.POST.get("buscar_seccion")
        notas=NotasDB.objects.filter(Grado__icontains=grado, Seccion__icontains=seccion)
        return render(request, "gestiones/ConsultaN.html", {"notas": notas})

    else:  
        notas = NotasDB.objects.all()
        ctx = {
            'notas':notas
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
                    'form':form
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
            nota = NotasDB.objects.get(id = id)      
            if request.method == 'GET':
                form = Notas(instance= nota)
                contx={
                    'form':form
                }

            else:
                
                form = Notas(request.POST, request.FILES, instance=nota)
                if form.is_valid():
                    form.save()
                    messages.success(request, f'Planilla de Notas del Grado {nota.Grado} de la Sección {nota.Seccion} fue Actualizado Correctamente')
                    return redirect("ConsultaN")

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
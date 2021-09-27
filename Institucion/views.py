from django.shortcuts import render, HttpResponse, redirect

#ViewClass----------------
from django.contrib.auth.views import LoginView

#BBDD----------------
from .models import *

#FormsModels----------------
from django.contrib.auth.forms import UserCreationForm
from .forms import *

#Auth----------------
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.http import HttpResponseRedirect

# Create your views here.

@login_required
def Home(request):
    return render(request, "Institucion/home.html")

def register_PA(request):
    
    if request.method == 'POST':
        form=UserRegisterForm_PA(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request, f'Usuario {username} Ha sido Creado Correctamente')
            return redirect("/")
            
    else:        
        form=UserRegisterForm_PA()
              
    ctx = { 'form':form }
    return render(request, "Institucion/register_PA.html", ctx)

def register_PD(request):
    
    if request.method == 'POST':
        form=UserRegisterForm_PD(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request, f'Usuario {username} Ha sido Creado Correctamente')
            return redirect("/")
            
    else:        
        form=UserRegisterForm_PD()
              
    ctx = { 'form':form }
    return render(request, "Institucion/register_PD.html", ctx)


class LoginUserSystem(LoginView):

    template_name = 'Institucion/login.html'
    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        usertype1 = self.request.POST['user_type1']
        username = self.request.POST['username']
        usertype2 = self.request.POST['user_type2']
        datos_user = form.get_user()
        if usertype1 == '0':
            is_PA = datos_user.is_PA
            if is_PA == True:
                return HttpResponseRedirect(self.get_success_url())

            else:
                username=form.cleaned_data['username']
                messages.error(self.request, f'Error de Login, el Usuario {username} no Existe o es Usuario PD')
                return redirect("/")

        if usertype2 == '1':
            is_PD = datos_user.is_PD
            if is_PD == True:
                return HttpResponseRedirect(self.get_success_url())

            else:
                username=form.cleaned_data['username']
                messages.error(self.request, f'Error de Login, el Usuario {username} no Existe o es Usuario PA')
                return redirect("/")

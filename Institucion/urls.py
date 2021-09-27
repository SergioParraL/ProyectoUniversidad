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
from django.conf import settings

#Static/Media----------------
from django.conf.urls.static import static

#Views----------------
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('Home/', views.Home, name="Home"),
    path('register_PA/', views.register_PA, name='register_PA'),
    path('register_PD/', views.register_PD, name='register_PD'),
    path('', views.LoginUserSystem.as_view(), name="login"),
    path('logout/', LogoutView.as_view(template_name='Institucion/logout.html'), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
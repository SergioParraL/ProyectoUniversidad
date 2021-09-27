from django import forms

class RegistroPA(forms.Form):

    nombres=forms.CharField()
    apellidos=forms.CharField()
    cedula=forms.IntegerField()
    Foto=forms.ImageField()  
    cargo=forms.CharField()
    edad=forms.IntegerField()
    direccion=forms.CharField()
    teln_Casa=forms.IntegerField()
    teln_movil=forms.IntegerField()
    email=forms.EmailField()


class RegistroPD(forms.Form):
    nombres=forms.CharField()
    cedula=forms.IntegerField()
    apellidos=forms.CharField()
    cedula=forms.IntegerField()
    Foto=forms.ImageField()
    materia=forms.CharField()
    edad=forms.IntegerField()
    direccion=forms.CharField()
    teln_Casa=forms.IntegerField()
    teln_movil=forms.IntegerField()
    email=forms.EmailField()



class RepRegistro(forms.Form):
    nombres=forms.CharField()
    apellidos=forms.CharField()
    cedula=forms.IntegerField()
    Foto=forms.ImageField()
    edad=forms.IntegerField()
    direccion=forms.CharField()
    teln_Casa=forms.IntegerField()
    teln_movil=forms.IntegerField()
    email=forms.EmailField()
 

class EstRegistro(forms.Form):
    nombres=forms.CharField()
    apellidos=forms.CharField()
    cedula=forms.IntegerField()
    Foto=forms.ImageField()
    edad=forms.IntegerField()
    altura=forms.IntegerField()
    peso=forms.IntegerField()
    talla_zapato=forms.IntegerField()
    talla_camisa=forms.IntegerField()
    talla_pantalon=forms.IntegerField()
    grado=forms.IntegerField()
    seccion=forms.CharField()

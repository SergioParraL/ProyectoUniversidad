from django.db import models


# Create your models here.


class PersonalAdm(models.Model):
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    cedula=models.IntegerField(max_length=8)
    Foto=models.ImageField()  
    cargo=models.CharField(max_length=15)
    edad=models.IntegerField(max_length=2)
    direccion=models.CharField(max_length=50)
    teln_Casa=models.IntegerField(max_length=11)
    teln_movil=models.IntegerField(max_length=11)
    email=models.EmailField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Personal Adiministrativo'
        verbose_name_plural='Personal Adiministrativos'


class PersonalDocente(models.Model):
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    cedula=models.IntegerField(max_length=8)
    Foto=models.ImageField()
    materia=models.CharField(max_length=30)
    edad=models.IntegerField(max_length=2)
    direccion=models.CharField(max_length=50)
    teln_Casa=models.IntegerField(max_length=11)
    teln_movil=models.IntegerField(max_length=11)
    email=models.EmailField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    


    class Meta:
        verbose_name='Personal Docente'
        verbose_name_plural='Personal Docentes'



class Representantes(models.Model):
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    cedula=models.IntegerField(max_length=8)
    Foto=models.ImageField()
    edad=models.IntegerField(max_length=2)
    direccion=models.CharField(max_length=50)
    teln_Casa=models.IntegerField(max_length=11)
    teln_movil=models.IntegerField(max_length=11)
    email=models.EmailField()
    #children = models.ManyToMany(Estudiantes)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Representante'
        verbose_name_plural='Representantes'



class Estudiantes(models.Model):
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    cedula=models.IntegerField(max_length=8)
    Foto=models.ImageField()
    edad=models.IntegerField(max_length=2)
    altura=models.FloatField(max_length=5)
    peso=models.FloatField(max_length=5)
    talla_zapato=models.IntegerField(max_length=2)
    talla_camisa=models.IntegerField(max_length=2)
    talla_pantalon=models.IntegerField(max_length=2)
    grado=models.IntegerField(max_length=1)
    seccion=models.CharField(max_length=1)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Estudiante'
        verbose_name_plural='Estudiantes'




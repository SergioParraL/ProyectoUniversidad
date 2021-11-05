from django.db import models

# Create your models here.

Grados_list = [
    
    (1, '1ero'),
    (2, '2do'),
    (3, '3ro'),
    (4, '4to'),
    (5, '5to'),
    (6, '6to'),
]

Secciones_list = [
    
    (1, 'A'),
    (2, 'B'),
    (3, 'C'),
    (4, 'D'),
    (5, 'E'),
    (6, 'F'),
    (7, 'G'),
    (8, 'H'),
]
 

Materias_list = [
    
    (1, 'Lenguaje'),
    (2, 'Comunicación y Cultura'),
    (3, 'Ciencias Naturales y Sociedad'),
    (4, 'Ciencias Sociales'),
    (5, 'Ciudadanía e Identidad'),
    (6, 'Educación Física, deporte y Recreación'),
    (7, 'Matemática'),
] 

Especialidades_list = [
    
    (1, 'Desarrollo Endogeno'),
    (2, 'Educación Física'),
    (3, 'Música'),
    (4, 'Teatro'),
    (5, 'Danza'),
    (6, 'Manualidades'),
    (7, 'Aula Integrada'),
    (8, 'Producción'),
    (9, 'CRA (Centro de Recursos para el Aprendizaje)'),
] 

class PersonalAdm(models.Model):
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    cedula=models.CharField(unique=True,max_length=12)
    foto=models.ImageField(upload_to='PerAD/%Y/%m/%d/', null=True)  
    cargo=models.CharField(max_length=15)
    edad=models.IntegerField()
    direccion=models.TextField(max_length=100)
    teln_Casa=models.CharField(max_length=11)
    teln_movil=models.CharField(max_length=11)
    email=models.EmailField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Personal Administrativo'
        verbose_name_plural='Personal Administrativos'


class PersonalDocente(models.Model):
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    cedula=models.CharField(unique=True,max_length=12)
    foto=models.ImageField(upload_to='PerDO/%Y/%m/%d/', null=True)
    materia=models.IntegerField(
        null=False, blank=False,
        choices=Materias_list,
        default=1
    )
    especialidades=models.IntegerField(
        null=False, blank=False,
        choices=Especialidades_list,
        default=1
    )    
    edad=models.IntegerField()
    direccion=models.TextField(max_length=100)
    teln_Casa=models.CharField(max_length=11)
    teln_movil=models.CharField(max_length=11)
    email=models.EmailField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    


    class Meta:
        verbose_name='Personal Docente'
        verbose_name_plural='Personal Docentes'



class Representantes(models.Model):
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    cedula=models.CharField(unique=True,max_length=12)
    foto=models.ImageField(upload_to='REP/%Y/%m/%d/', null=True)
    edad=models.IntegerField()
    direccion=models.TextField(max_length=100)
    teln_Casa=models.CharField(max_length=11)
    teln_movil=models.CharField(max_length=11)
    email=models.EmailField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Representante'
        verbose_name_plural='Representantes'

    def __str__(self):
        return self.cedula


class Estudiantes(models.Model):
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    cedula=models.CharField(unique=True,max_length=12)
    foto=models.ImageField(upload_to='EST/%Y/%m/%d/', null=True)
    edad=models.IntegerField()
    altura=models.FloatField(max_length=5)
    peso=models.FloatField(max_length=5)
    talla_zapato=models.IntegerField()
    talla_camisa=models.CharField(max_length=2)
    talla_pantalon=models.IntegerField()
    grado=models.IntegerField(
        null=False, blank=False,
        choices=Grados_list,
        default=1
    )
    seccion=models.IntegerField(
        null=False, blank=False,
        choices=Secciones_list,
        default=1
    )
    fecha_nac=models.DateField()
    Rep=models.ForeignKey(Representantes, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Estudiante'
        verbose_name_plural='Estudiantes'




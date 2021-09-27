from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


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

class SystemUser(AbstractUser):
    username = models.CharField('Nombre de Usuario',
        max_length=30,
        unique=True,
        help_text='Requiere. 30 Caracteres o menos. Entre: Letras, digitos númericos and @/./+/-/_ solamente.',
        error_messages={
            'unique':'Un Usuario ya está registrado con este nombre de Usuario'
        },
    )
    email = models.EmailField('Email del Usuario', unique=True, max_length=50)
    is_staff = models.BooleanField('Estado de Administrador',
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField('Activado',
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_PA = models.BooleanField('Estado de Usuario PA',
        default=False,
        help_text='Esta opcion, permite el acceso a Usuario de tipo PA: Personal Administrativo',
    )
    is_PD = models.BooleanField('Estado de Usuario PD',
        default=False,
        help_text='Esta opcion, permite el acceso a Usuario de tipo PD: Personal Docente',
    )


    REQUIRED_FIELD = ['email', 'is_PA', 'is_PD']

    def __str__(self):
        return f'El usuario es {self.username} y su correo {self.email}'


class PA_profile(models.Model):
    usuario = models.OneToOneField(SystemUser, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    cedula = models.CharField(unique=True, max_length=12)
    foto = models.ImageField(upload_to='PerAD/%Y/%m/%d/', null=True, blank=True)  
    cargo = models.CharField(max_length=15)
    edad = models.IntegerField()
    direccion = models.TextField(max_length=100)
    teln_Casa = models.CharField(max_length=11)
    teln_movil = models.CharField(max_length=11)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Personal Administrativo2'
        verbose_name_plural = 'Personal Administrativos2'


class PD_profile(models.Model):
    usuario = models.OneToOneField(SystemUser, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    cedula = models.CharField(max_length=12)
    foto = models.ImageField(upload_to='PerAD/%Y/%m/%d/', null=True)  
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
    edad = models.IntegerField()
    direccion = models.TextField(max_length=100)
    teln_Casa = models.CharField(max_length=11)
    teln_movil = models.CharField(max_length=11)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    


    class Meta:
        verbose_name = 'Personal Docente2'
        verbose_name_plural = 'Personal Docentes2'
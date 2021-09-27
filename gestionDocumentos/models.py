from django.db import models


# Create your models here.


Docs_tipo = [
    
    (1, 'Boletin'),
    (2, 'Constancia'),
    (3, 'Planilla'),
    (4, 'Convocatoria'),
    (5, 'Otro'),
]

Docs_format = [
    
    (1, 'Word'),
    (2, 'Excel'),
    (3, 'PowerPoint'),
    (4, 'PDF'),
    (5, 'LibreOffice'),
    (6, 'Otro'),
]


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
 
    

class DocsDB(models.Model):
    
    Nombre_Documento=models.CharField(max_length=30)
    Documento=models.FileField(
        upload_to='uploads/Docs/%Y/%m/%d/', null=True)  
    Tipo=models.IntegerField(
        null=True, blank=False,
        choices=Docs_tipo,
        default=2
    )
    Formato=models.IntegerField(
        null=False, blank=False,
        choices=Docs_format,
        default=1
    )
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Documento Administrativo'
        verbose_name_plural='Documentos Administrativos'
        
    def __str__(self):
        return self.Nombre_Documento
    
    
class NotasDB(models.Model):
    
    Grado=models.IntegerField(
        null=False, blank=False,
        choices=Grados_list,
        default=1
    )
    Seccion=models.IntegerField(
        null=False, blank=False,
        choices=Secciones_list,
        default=1
    )
    #Momento=models.CharField(max_length=3)
    Documento=models.FileField(upload_to='uploads/Notas/%Y/%m/%d/', null=True)  
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Nota'
        verbose_name_plural='Notas'
        
    def __str__(self):
        return self.Grado
    


from django import template 

register = template.Library() 

def concat_Materia(Gradonum): 
    Materias_list = [
        
        ('Lenguaje'),
        ('Comunicación y Cultura'),
        ('Ciencias Naturales y Sociedad'),
        ('Ciencias Sociales'),
        ('Ciudadanía e Identidad'),
        ('Educación Física, deporte y Recreación'),
        ('Matemática'),
    ] 

    Materia = Gradonum - 1
    select_materia = Materias_list[Materia]

    return select_materia

register.filter("concat_Materia",concat_Materia)


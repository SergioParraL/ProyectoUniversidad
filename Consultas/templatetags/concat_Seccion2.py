from django import template 

register = template.Library() 


def concat_Seccion2(Gradonum):
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

    Seccion = Gradonum - 1
    select_sec = Secciones_list[Seccion]

    return select_sec

register.filter("concat_Seccion2",concat_Seccion2)



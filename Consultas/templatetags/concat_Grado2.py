from django import template 

register = template.Library() 

def concat_Grado2(Gradonum): 
    value_2 = ''
    Grados_list = [
        
        ('1ero'),
        ('2do'),
        ('3ro'),
        ('4to'),
        ('5to'),
        ('6to'),
    ]

    Grado = Gradonum - 1
    select_grado = Grados_list[Grado]

    return select_grado

register.filter("concat_Grado2",concat_Grado2)

